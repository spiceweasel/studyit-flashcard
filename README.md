studyit-flashcard
=================

<h2>Introduction</h2>
<p>Is a web based flashcard application that organizes card content based upon the Table of Contents of the book being studied.  This project is written in Python 2.7 using Django version 1.5.x and JQuery Mobile as the front end.</p>

<h3>Purpose</h3>
<p>This project was created in the beginning of my senior year of college to assist in studying under an anticipated heavy course load.  The ideas was to make flashcard system that allowed structured and incremental studying. I determined that an organization scheme based upon the existing structure of the books was a good choice for capturing the material (since most professors teach from a required text-book) and for studying (since the author already has organized the material in a manner that builds upon itself).  It proved to be more than suitable for my needs.</p>

<h3>Project Status</h3>
<p>Studyit-flashcard works well for it's designed purpose and is fully functional.  I have successfully used it with 10+ books and over 1500 flashcards.</p>

<h2>Features</h2>
<ul>
<li>Keep track of flashcards based upon the existing organization scheme of a book.</li>
<li>Books can be browsed based on their included categories.</li>
<li>Flashcards can be browsed by Chapter and section.</li>
<li>Flashcards can be studied by Chapter or section.</li>
<li>Text or images can be applied to the front or back side of the flashcard.</li>
<li>Uses HTML 5 media capture to allow users to take images directly from the camera on their smart devices.</li>
</ul>


<h2>TODO List</h2>
<ul>
<li>Unit testing.</li>
<li>Study using included sections.</li>
<li>Detect correct/incorrect responses and give more advanced cards as the student progresses</li>
<li>Reorganize flashcard difficutly levels based on numbers not categories.</li>
<li>Add modal selection button for difficulty levels instead of a drop-down list.</li>
<li>JQuery Mobile slide out panel to access options for the flashcard card being viewed.</li>
<li>Support for multiple isolated users on the same server.</li>
<li>Automated book backup and restore.</li>
<li>Add admin panel links to assist in book chapter and section creation.</li>

</ul>

<h3>Known Bugs/Issues</h3>
<ul>
<li>When choosing study by chapter, the first displayed will have a non-matching answer.  I have not had a chance to investigate this issues.  Workaround by selecting correct or incorrect to jump to the next card.</li>

</ul>


