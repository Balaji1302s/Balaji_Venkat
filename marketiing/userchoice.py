from validation import New_Registration

from validation import Login
class Userchoice():
    @classmethod
    def userChoice():
        User_view.greetings()
        flag = True
        while flag:   
            
            choice = User_view.user_choice()
            if choice == 1:
                 New_Registration.new_user()
            
            elif choice == 2:
                Login.login()
             
            else:
                print("There is no Such Kind of action")
            

