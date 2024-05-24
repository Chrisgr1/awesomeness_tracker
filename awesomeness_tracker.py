
class AwesomenessOverload(Exception):
    """The user's awesomeness has overloaded the system. You are most excellent. We're not worthy, we're not worthy, we're not worthy."""

class AwesomenessCheck():
    def __init__(self, name, awesomeness_level=7000):
         self.name = name
         if not isinstance(awesomeness_level, int):
            raise TypeError("Awesomeness level must be an integer.")
         self.awesomeness_level = awesomeness_level

    def set_awesomeness_level(self, level):
        if not isinstance(level, int):
            raise TypeError("Awesomeness level must be an integer.") 
        self.awesomeness_level = level

    def develop_awesomeness_level(self):
         self.awesomeness_level += 1000
         print("The data indicate you just became significantly more awesome.")
    
    def get_awesomeness_level(self):
            try:
                if self.awesomeness_level < 9000:
                     print("Awesomeness level is within acceptable limits. As you were, netizen.")

                if self.awesomeness_level > 9000:
                    raise AwesomenessOverload("The user's awesomeness has overloaded the system.")
                
            except AwesomenessOverload as e:
                print(f"Exception: {e}")
                
                

            finally:
                print("Awesomeness check completed.")


alice = AwesomenessCheck("Alice", 5000)
alice = AwesomenessCheck("Alice", 5000)
alice.get_awesomeness_level()
alice.develop_awesomeness_level()
alice.get_awesomeness_level()


