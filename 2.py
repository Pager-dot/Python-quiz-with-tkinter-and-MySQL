# this is a quiz program 

print('Select the following subject to imporve on :')
a = str(input('A) Maths B) Physics C) Chemisty : '))
def maths():
    print('''Math practice is important. Once you understand the concept, you have to nail down the mechanics. And often, 
it’s the practice that finally helps the concept click. Either way, math requires more than just reading formulas on a page. 
Daily practice can be tough to implement, especially with a math-averse child. This is a great time to bring out the game-based 
learning mentioned above. Or find an activity that lines up with their current lesson. Are they learning about squares? Break out 
the math link cubes and create them. Whenever possible, step away from the worksheets and flashcards and find practice elsewhere.''')

def Physics():
    print(''' If you are struggling with learning physics, the worst thing you can do is try going at it alone. There are dozens of different 
ways you can get help. Seek and use any resources available to you to get a better understanding of the physics material.

While some options might cost money, you are also bound to find several free resources. For example, you could try:

1) Setting up an after-school consultation with your physics teacher
2) Setting up physics study groups
3) Hiring private physics tutors
4) Third-party resources such as physics websites, libraries, and education websites
5) Enrol for physics tuition services in Singapore

The most viable option today is hiring a private physics tutor. Kungfu Physics offers 
some of the best physics tuition services in Singapore via tuition centres. This means that you will get
access to some of the best physics tutors in the country as well as a chance to form a physics study group with other 
students in the sessions.''')

def Chemistry():
    print('''Chemistry is one of those classes you either love or dread. At the high school level chemistry is usually not a required course
it's an elective. However, most reputable colleges require all undergraduate students to take at least one chemistry course as a 
prerequisite to graduation. If you plan on pursuing a career in medicine, engineering, or a field of natural science, then you're 
likely going to be required to take at least one chemistry course before you graduate. Chemistry is a challenging subject for most 
people, but it doesn't have to be. The number one reason people struggle with chemistry is that they don't approach it the right way.
Below we'll explore proven strategies and techniques that will, if applied, improve your ability to study and learn chemistry.

Review and Study Material Before Going to Class
In a traditional learning model, students arrive at class, the instructor introduces the material, expounds on relevant 
concepts, assigns follow up readings and assignments, and ends class. Students are then expected to go home, review their 
class notes, attempt to complete assigned readings and assignments, actually learn what was taught in class (which doesn't 
always happen), come to class the following week with any questions they have from the previous lecture, and be ready to move 
on and explore new material and concepts. The problem with this model is that it's ineffective, especially with subjects and 
material that are challenging to learn.

The best way to learn chemistry is to come to each lecture having already read and studied the material that is going to be 
presented that day. This method of learning is known as the 'Flipped Classroom', sometimes referred to as 'Class Reversed', 
and it is a growing trend for teaching many subjects in schools and colleges nationwide. This model is especially effective for 
learning (and teaching) chemistry for several reasons. First, it gets students to come to class having already studied the material 
to be presented. Second, arriving at class already familiar with the subject matter, students are able to follow along and 
understand what is being taught. If students did not understand concepts from their studies, they are able to ask questions during 
the relevant lecture. Finally, classroom time is used more effectively as a learning tool. Students come away from each lecture 
with a much better understanding of course concepts and with fewer questions.

Studying your chemistry assignments, readings, and material before going to each class is one of the most effective 
strategies for learning chemistry.

Seek Understanding
As with any of the sciences, there is a lot of new information to learn and memorize in chemistry. In fact, there 
is so much new information you'll be presented with as you begin to study chemistry that you'll get bogged down quickly 
if you get caught up trying to memorize all the details. First focus on gaining understanding of fundamental concepts. 
Once you have a sound understanding of the fundamentals, you can spend time memorizing the details. Also, as you master 
the fundamentals of chemistry and gain understanding of the concepts, you'll find it much easier to memorize everything else.

Remember, memorization should never replace understanding. Seek to gain understanding first.

Take Good Notes
Attending class regularly and paying attention is important, but it's not enough. As you study chemistry, it's necessary to 
take copious, intelligible notes that further your understanding of the concepts being discussed. Note taking is of particular 
importance to the study of chemistry for the following reasons.

Note taking also forces you to write things down. The formulas and equations you'll be introduced to as you study chemistry 
will be far easier to remember and understand after you've written them down.
Taking good notes, and then reviewing those notes, will help you to determine what you do and don't understand.
Make sure your note taking is organized. Taking organized notes will help you review lectures effectively and prepare for exams.
Note taking will enable you to participate in study groups. The better your notes, the better you'll be able to 
participate and contribute to your study group.
When taking notes, don't just focus on what your instructor writes on the board. Listen and copy down all key verbal 
points and concepts discussed during the lecture.

After each lecture take a few minutes to review your notes. Make sure you understand all the concepts covered in the 
lecture. Use your textbook to improve your notes and understanding of key concepts covered.''')
if a == "A" :
    maths()
else:
    print('Wrong input')
if a == "B" :
    Physics()
else:
    print('Wrong input')
if a == "C" :
    Chemistry()
else:
    print('Wrong input')