#!/usr/bin/env python3
"""
Expense Tracker CLI - Track expenses, generate reports, and visualize spending patterns
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import argparse
import sys

# Storage file
DATA_FILE = "expenses.json"

# Category colors for visualization
CATEGORIES = [
    "Food", "Transportation", "Entertainment", "Shopping", 
    "Bills", "Healthcare", "Education", "Other"
]


def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)


def add_expense(amount, category, description, date=None):
    """Add a new expense"""
    expenses = load_expenses()
    
    if category not in CATEGORIES:
        print(f"Warning: '{category}' is not a standard category.")
        print(f"Standard categories: {', '.join(CATEGORIES)}")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    expense = {
        'id': len(expenses) + 1,
        'amount': float(amount),
        'category': category,
        'description': description,
        'date': date or datetime.now().strftime('%Y-%m-%d'),
        'timestamp': datetime.now().isoformat()
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✓ Expense added: ${amount:.2f} - {category} - {description}")


def list_expenses(limit=None, category=None, days=None):
    """List expenses with optional filters"""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    # Apply filters
    filtered = expenses
    
    if category:
        filtered = [e for e in filtered if e['category'].lower() == category.lower()]
    
    if days:
        cutoff = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        filtered = [e for e in filtered if e['date'] >= cutoff]
    
    # Sort by date (newest first)
    filtered.sort(key=lambda x: x['date'], reverse=True)
    
    if limit:
        filtered = filtered[:limit]
    
    if not filtered:
        print("No expenses match your filters.")
        return
    
    print(f"\n{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
    print("-" * 70)
    
    for expense in filtered:
        print(f"{expense['id']:<5} {expense['date']:<12} {expense['category']:<15} "
              f"${expense['amount']:<9.2f} {expense['description']}")
    
    print(f"\nTotal: ${sum(e['amount'] for e in filtered):.2f}")


def delete_expense(expense_id):
    """Delete an expense by ID"""
    expenses = load_expenses()
    
    # Find expense
    expense = next((e for e in expenses if e['id'] == expense_id), None)
    
    if not expense:
        print(f"Error: Expense with ID {expense_id} not found.")
        return
    
    print(f"Delete: ${expense['amount']:.2f} - {expense['category']} - {expense['description']}?")
    response = input("Confirm (y/n): ")
    
    if response.lower() == 'y':
        expenses = [e for e in expenses if e['id'] != expense_id]
        save_expenses(expenses)
        print("✓ Expense deleted.")
    else:
        print("Deletion cancelled.")


def generate_report(period='month'):
    """Generate expense report"""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses to report.")
        return
    
    # Determine date range
    now = datetime.now()
    if period == 'week':
        cutoff = (now - timedelta(days=7)).strftime('%Y-%m-%d')
        title = "Last 7 Days"
    elif period == 'month':
        cutoff = (now - timedelta(days=30)).strftime('%Y-%m-%d')
        title = "Last 30 Days"
    elif period == 'year':
        cutoff = (now - timedelta(days=365)).strftime('%Y-%m-%d')
        title = "Last 365 Days"
    else:
        cutoff = None
        title = "All Time"
    
    # Filter expenses
    if cutoff:
        filtered = [e for e in expenses if e['date'] >= cutoff]
    else:
        filtered = expenses
    
    if not filtered:
        print(f"No expenses in {title.lower()}.")
        return
    
    # Calculate statistics
    total = sum(e['amount'] for e in filtered)
    avg_per_expense = total / len(filtered)
    
    # Group by category
    by_category = defaultdict(float)
    for expense in filtered:
        by_category[expense['category']] += expense['amount']
    
    # Print report
    print(f"\n{'='*60}")
    print(f"EXPENSE REPORT - {title}")
    print(f"{'='*60}\n")
    
    print(f"Total Expenses: ${total:.2f}")
    print(f"Number of Transactions: {len(filtered)}")
    print(f"Average per Transaction: ${avg_per_expense:.2f}")
    
    print(f"\n{'SPENDING BY CATEGORY':^60}")
    print("-" * 60)
    print(f"{'Category':<20} {'Amount':<15} {'Percentage'}")
    print("-" * 60)
    
    # Sort categories by amount
    sorted_categories = sorted(by_category.items(), key=lambda x: x[1], reverse=True)
    
    for category, amount in sorted_categories:
        percentage = (amount / total) * 100
        print(f"{category:<20} ${amount:<14.2f} {percentage:>5.1f}%")
    
    print("=" * 60)


def visualize_spending(period='month'):
    """Create ASCII bar chart of spending by category"""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses to visualize.")
        return
    
    # Determine date range
    now = datetime.now()
    if period == 'week':
        cutoff = (now - timedelta(days=7)).strftime('%Y-%m-%d')
        title = "Last 7 Days"
    elif period == 'month':
        cutoff = (now - timedelta(days=30)).strftime('%Y-%m-%d')
        title = "Last 30 Days"
    elif period == 'year':
        cutoff = (now - timedelta(days=365)).strftime('%Y-%m-%d')
        title = "Last 365 Days"
    else:
        cutoff = None
        title = "All Time"
    
    # Filter expenses
    if cutoff:
        filtered = [e for e in expenses if e['date'] >= cutoff]
    else:
        filtered = expenses
    
    if not filtered:
        print(f"No expenses in {title.lower()}.")
        return
    
    # Group by category
    by_category = defaultdict(float)
    for expense in filtered:
        by_category[expense['category']] += expense['amount']
    
    # Create visualization
    print(f"\n{'='*70}")
    print(f"SPENDING VISUALIZATION - {title}")
    print(f"{'='*70}\n")
    
    max_amount = max(by_category.values())
    max_bar_width = 50
    
    sorted_categories = sorted(by_category.items(), key=lambda x: x[1], reverse=True)
    
    for category, amount in sorted_categories:
        bar_width = int((amount / max_amount) * max_bar_width)
        bar = '█' * bar_width
        print(f"{category:<15} {bar} ${amount:.2f}")
    
    total = sum(by_category.values())
    print(f"\n{'Total:':<15} ${total:.2f}")
    print("=" * 70)


def show_categories():
    """Display available categories"""
    print("\nStandard Categories:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"  {i}. {category}")
    print("\nYou can also use custom categories when adding expenses.")


def main():
    parser = argparse.ArgumentParser(
        description='Expense Tracker CLI - Track and analyze your spending',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s add 45.50 Food "Lunch at cafe"
  %(prog)s add 120 Bills "Electric bill" --date 2024-01-15
  %(prog)s list --limit 10
  %(prog)s list --category Food --days 7
  %(prog)s report --period month
  %(prog)s visualize --period week
  %(prog)s delete 5
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Add expense
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('amount', type=float, help='Expense amount')
    add_parser.add_argument('category', help='Expense category')
    add_parser.add_argument('description', help='Expense description')
    add_parser.add_argument('--date', help='Date (YYYY-MM-DD), defaults to today')
    
    # List expenses
    list_parser = subparsers.add_parser('list', help='List expenses')
    list_parser.add_argument('--limit', type=int, help='Limit number of results')
    list_parser.add_argument('--category', help='Filter by category')
    list_parser.add_argument('--days', type=int, help='Show expenses from last N days')
    
    # Delete expense
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('id', type=int, help='Expense ID to delete')
    
    # Generate report
    report_parser = subparsers.add_parser('report', help='Generate expense report')
    report_parser.add_argument('--period', choices=['week', 'month', 'year', 'all'], 
                               default='month', help='Report period (default: month)')
    
    # Visualize spending
    viz_parser = subparsers.add_parser('visualize', help='Visualize spending patterns')
    viz_parser.add_argument('--period', choices=['week', 'month', 'year', 'all'], 
                            default='month', help='Visualization period (default: month)')
    
    # Show categories
    subparsers.add_parser('categories', help='Show available categories')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Execute commands
    try:
        if args.command == 'add':
            add_expense(args.amount, args.category, args.description, args.date)
        elif args.command == 'list':
            list_expenses(args.limit, args.category, args.days)
        elif args.command == 'delete':
            delete_expense(args.id)
        elif args.command == 'report':
            generate_report(args.period)
        elif args.command == 'visualize':
            visualize_spending(args.period)
        elif args.command == 'categories':
            show_categories()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()