# The-Blind-s-Eye
THE BLIND’S EYE aims towards development in the field of AI (Artificial Intelligence). 
Our main and sole purpose to develop this project to help the visually challenged (Blind) 
people. Our project focuses on safety to Detect and Recognize people using Raspberry pi3 
enabled with camera module, ArduCam module, power bank or any suitable portable power 
supply to provide efficient power supply to the Pi and earphones. It requires an Internet 
connection to operate. We have also planned to provide basic day to day features to help the 
blind people using voice input through earphone’s mic and output through earphones or any 
compatible headphones with mic. Many more features can be customized and added to the 
Rpi3 to make it more efficient and much more user-friendly. This system had to be made as 
light-weight as possible because it is to be used on a daily basis. 

. Aims & Objectives: The project aims and objectives that will be achieved after 
completion of this project are as follows- 

. Detection of human faces 

. Recognition of detected faces by making near accurate 
predictions 

. Detection and Recognition of a few objects 

. Hot-word activated Virtual assistant(AI) 

There are 2 modules in the Project 

 1-Face detection and recognition 

2-Virtual Assistant 

 As the targeted users are mostly visually impaired ,they interact with the system purely 
through the means of audio. 

Features: 

. It gives you a Personal Virtual Assistant (PVA). 
. It acts as a portable-smart device. 
. Fast decision making. 
. Learning Ability 


 It works as follows- 

Face Detection and Recognition works basically like – 

. First, look at a picture and find all the faces in it 
. Second, focus on each face and be able to understand that even if a face is turned in a 
weird direction or in bad lighting, it is still the same person. 
. Third, be able to pick out unique features of the face that you can use to tell it apart 
from other people like how big the eyes are, how long the face is, etc. 
. Finally, compare the unique features of that face to all the people you already know to 
determine the person’s name. 

The Face Recognition module works as follows- 

. Firstly the sample images of people to be recognized are given to the Python script for 
checking against the real time feed 
. When the user wants to recognize a person he would have to say the hot word to 
awaken the virtual assistant and then say scan or recognize. 
. Then the face recognition script would run and check the person in the frame against 
the sample images provided. 
. Every sample image would be associated with a name. So when the program would 
find a match, the AI would tell the user the name of that person through the 
Earphones. 

The Virtual Assistant module works as follows- 

. Firstly, the user has to start the system by switching on the button provided. 
. As soon as the system starts, it will directly boot into the Virtual Assistant python 
script 
. It will give a initial welcome message. 
. After which user will speak command. 
. This will invoke Google Speech to text API and convert speech to text and it will 
check text forknown keywords. 
. It will then execute command written in corresponding Python Script and then it will 
return answer using Google Text to Speech Voice Engine 
. If the user is done with the use of the system then he can switch it off or he can give 
other commands as well. 

