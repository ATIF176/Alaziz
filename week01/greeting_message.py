def greeting_message():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    if user_age < 15:
        print(str(user_name) + "! 🌈 Wishing you a day filled with laughter, joy, and endless adventures! May your youthful spirit continue to shine bright!")
    elif user_age > 15 and user_age < 33:
        print(str(user_name) + "! 🎉 Embrace the energy and possibilities that come with being in your twenties and thirties. Make every moment count and create memories that last a lifetime!")
    elif user_age > 33 and user_age < 45:
        print(str(user_name) + "! 🌟 Life's journey is a beautiful ride, and your forties are a time to savor wisdom, growth, and new horizons. Here's to the amazing chapters ahead!")
    else:
        print(str(user_name) + "! 🌺 Embracing the richness of experience and the beauty of every moment. Your journey has been remarkable, and the best is yet to come. Cheers to the adventures ahead!")

greeting_message()