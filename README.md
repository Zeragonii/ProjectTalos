# Project: Talos
A college run project inspired by the first ever recorded robot, the mythical Automaton: Talos.

This readme will provide a step by step instruction guide on how to utilise this set of scripts on running Project: Talos.

NOTE: This readme is designed to instruct users on the basic operation and setup of the pre-built Talos MK.I Automaton situated in Knowsley Community College. This code CAN be reworked to power other web based robots, however your milage will vary and I am only able to provide support for the primary unit this code was written for.


Step 1: Requirements

There arent many requirements to run this project, however if for whatever reason the master Pi becomes corrupt then this will serve as a base point for regaining full functionality. The main software used is in the form of LAMP (Linux Apache MySQL and PHP), I installed these manually as there was already a Linux distro installed on the Pi (Raspbian) and I didn't feel like redoing the whole thing from scratch. Apache2, with its latest security updates is used as the backbone communication engine between the controlling client and the automaton itself. MySQL is my cheap solution to the barrier between client and server, I used the database to translate client actions into server responses. That will be explained later on in the code comments. PHP is needed as it adds a very useful layer of functionality to the Apache site, mainly database transactions. And that's pretty much it for the requirements, there's a prebuilt library for the servo controller but that should already be included in the file so I wont talk too much about that.

Step 2: Build the thing

It's a pretty simple and obvious one, you need a robot in order to code one. So when you have a fully constructed setup like the MK.I then feel free to proceed to step 3. If any detailed information is required on the components used then file in an Issue/Request and I'll update/address things as and when needed.

Step 3: Code the thing

Once you've built your marvellous automaton you're going to want to write out the code for it, I've done most of the legwork for the MK.I but if you plan on iterating on my work then you're going to have to make changes to things like servo calling and various numbers, this will be explained much more in-depth in the code itself. Again, if you would like my help feel free to submit an Issue/Request and I'll address it accordingly. 

Step 4: INITIALISE

Now that you have your code and your robot you will need to plug it all in and make sure it works, I made various initialisation functions to give the servos and motor a little nudge to see if they were awake (Mainly because the motor ESC doesn't wake up unless it recieves a little jiggle down the ole' PWM feed.) 
For the Talos MK.I firing up the code is pretty straight forward, Apache runs on boot and the config should be changed to point towards the WWW folder inside the Talos directory. Because I don't like bash scripts, or well don't trust myself with them, this next part has to be done manually. Inside of the Talos directory there will be a file called "Runtime.py", you want to point Terminal to the Talos folder and run "sudo python Runtime.py" and it should do the rest. 

Step 5: Play your heart away

By this point the automaton should be up and running, so fire up Chrome (I'd say your favourite browser but if your favourite isn't chrome then you're just wrong.) and navigate to whatever the Pi's local IP address is, should be easy enough, this will give you a lovely blotch of colours. These colours are pretty much just placeholders for, what was going to be, Forward Backward, Left and Right arrows, as well as a camera feed on the main section. Time constraints prevented us from achieving that goal though, sadly. 
