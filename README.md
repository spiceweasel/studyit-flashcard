studyit-flashcard
=================

<h2>Introduction</h2>
<p>Is a web based flashcard application that organizes card content based upon the Table of Contents of the book being studied.  This project is written in Python 2.7 using Django version 1.5.x and JQuery Mobile as the front end.</p>

<h3>Purpose</h3>
<p>This project was created in the beginning of my senior year of college to assist me in studying under an anticipated heavy course load.  The ideas was to make flash-card system based on the organization method most professors use to present information to their students.  Since most of my professors taught along with the reading material I felt that organization based upon a books was a good choice.  It proved to be more than suitable for my needs.</p>

<h3>Project Status</h3>
<p>Studyit-flashcard works well for it's designed purposes and is a fully functional.  I have successfully used it with 10+ books and over 1500 flashcards.</p>

<h2>Features</h2>
<ul>
<li>Keep track of your flashcards based upon the existing organization scheme of the book you are studying from.</li>
<li>Books have chapter and section entries which are used for browsing and study sessions.</li>
<li>Named categories are available to assist users in browsing and searching books.</li>
<li>Flashcards can have text or images for the front or back of the flashcard.</li>
<li>Uses HTML 5 media capture to allow users to take images directly from the camera on their smart devices.</li>
<li>Study flashcards from one of two groups study by chapter and study by section.</li>
</ul>


<h2>TODO List</h2>
<ul>
<li>Create a modularized version of this project conforming to Django.</li>
<li>Unit testing.</li>
<li>Enhanced study features which include:
  <ul><li>Study using included sections.</li><li>Detect correct/incorrect responses and give more advanced cards as the student progresses</li><li>Reorganize flashcard difficutly levels based on numbers not categories.</li><li>Add modal selection button for difficulty levels instead of a drop-down list.</li><li>Slide out panel to access options for the flashcard card being viewed.</li><li>Support for multiple users on the same server.</li><li>Automated book backup and restore.</li><li>Add admin panel links to assist in book chapter and section creation.</li>
  </ul>
<li>
</ul>

<h3>Known Bugs/Issues</h3>
<ul>
<li>When choosing study by chapter, the first displayed will have a non-matching answer.  I have not had a chance to investigate this issues.  Pushing correct or incorrect to get the next card worked well for my purposes.</li>

</ul>


