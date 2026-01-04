class Person:
    name = "John Doe"
    age = 30
    occupation = "Software Developer"
    country = "USA"
    city = "New York"
    hobby = "Photography"
    favorite_food = "Pizza"
    favorite_color = "Blue"
    height_cm = 175
    weight_kg = 70
    is_employed = True
    has_driver_license = True
    languages_spoken = ["English", "Spanish"]
    marital_status = "Single"
    number_of_children = 0
    annual_income = 80000
    education_level = "Bachelor's Degree"
    favorite_sport = "Basketball"
    pet_name = "Buddy"
    pet_type = "Dog"
    social_media_handle = "@johndoe"
    phone_number = "123-456-7890"
    email_address = "john.doe@example.com"

    def introduce(self):
        return f"Hello, my name is {self.name}. I am a {self.age}-year-old {self.occupation} from {self.city}, {self.country}."
    
    def get_hobby(self):
        return f"My hobby is {self.hobby}."
    
    def get_favorite_food(self):
        return f"My favorite food is {self.favorite_food}."
    
    def get_contact_info(self):
        return f"You can reach me at {self.email_address} or {self.phone_number}."
    
    def get_personal_info(self):    
        return {
            "Name": self.name,
            "Age": self.age,
            "Occupation": self.occupation,
            "Country": self.country,
            "City": self.city,
            "Hobby": self.hobby,
            "Favorite Food": self.favorite_food,
            "Favorite Color": self.favorite_color,
            "Height (cm)": self.height_cm,
            "Weight (kg)": self.weight_kg,
            "Employed": self.is_employed,
            "Driver's License": self.has_driver_license,
            "Languages Spoken": self.languages_spoken,
            "Marital Status": self.marital_status,
            "Number of Children": self.number_of_children,
            "Annual Income": self.annual_income,
            "Education Level": self.education_level,
            "Favorite Sport": self.favorite_sport,
            "Pet Name": self.pet_name,
            "Pet Type": self.pet_type,
            "Social Media Handle": self.social_media_handle,
            "Phone Number": self.phone_number,
            "Email Address": self.email_address
        }
    

# Example usage:person = Person()
def main():
    person = Person()
    
    print(person.introduce())
    print(person.get_hobby())
    print(person.get_favorite_food())
    print(person.get_contact_info())


main()