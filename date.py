#import time;
#localtime = time.asctime(time.localtime(time.time()))
#print("the current time is",localtime)
#my_list=["zero","two","one"]
#print("elements of list,my_list are;")
#for ml in my_list:
 #   print(ml)
#new_list=["three","four"]
#nlist= my_list+new_list
#print(nlist)
#my_tuple=("ss","dd","www")
#print("my_tuple")
#print("every element in tuple")
#for item in my_tuple:
 #   print(item)
#squares={1:1,2:4,3:9,4:16,5:25}
#print(squares.pop(4))
#print(squares.popitem())
#print(squares.clear())
#del squares
# class Car():
#     def __init__(self):
#         self.__fuel = 100  # private variable
#         self._speed = 0  # protected variable
#     def start(self):
#         self._accelerate()
#
#     def _accelerate(self):
#         self.__fuel -= 5
#         self._speed += 10
#     def get_fuel(self):
#         return self.__fuel
# my_car= Car()
# my_car.start()
# print(my_car._speed) # accessing protected variable
# print(my_car.get_fuel()) # accessing private variable
import random

# Dictionary containing information about the college
college_info = {
    "programs": ["Computer Science", "Electrical Engineering", "Business Administration", "B.com", "MLS", "Psychology"],
    "admission_requirements": "To apply, you need to submit your high school transcripts and a letter of recommendation.",
    "contact": "For further inquiries, you can contact us at 9317872934,or at mail ggi2021.1911@ggi.ac.in."
}


# Function to handle user queries
def college_enquiry(query):
    if "programs" in query:
        return "We offer programs in " + ", ".join(college_info["programs"]) + "."
    elif "admission" in query:
        return college_info["admission_requirements"]
    elif "contact" in query:
        return college_info["contact"]
    else:
        return "I'm sorry, I couldn't understand your query. Please ask about programs, admission, or contact information."


# Main function to run the chatbot
def main():
    print("Welcome to GGI College Enquiry Bot!")
    print("Ask me about our programs, admission process, or contact information. To exit, type 'bye'.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("College Enquiry Bot: Goodbye! Have a great day.")
            break

        response = college_enquiry(user_input)
        print("College Enquiry Bot:", response)


# Run the chatbot
if __name__ == "_main_":
    main()
