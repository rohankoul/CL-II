
predicates 
        repeat
        age_group(integer)
        genre_c(integer)
        genre_y(integer)
        genre_o(integer)
        genre_sel_c(integer)
	genre_sel_f(integer)
	genre_sel_c_super(integer)
	genre_sel_f_pri(integer)
	genre_sel_a(integer)
	genre_sel_c_crime(integer)
	genre_sel_c_scifi(integer)
	genre_sel_f_magic(integer)
	genre_sel_f_moral(integer)
	genre_sel_a_math(integer)
	genre_sel_a_chem(integer)
	genre_sel_a_bio(integer)
	genre_sel_n(integer)
	genre_sel_b(integer)
	genre_sel_m(integer)
	genre_sel_n_mys(integer)
	genre_sel_n_fan(integer)
	genre_sel_n_rom(integer)
	genre_sel_b_autobio(integer)
	genre_sel_b_bio(integer)
	genre_sel_m_fash(integer)
	genre_sel_m_spor(integer)
	genre_sel_m_gad(integer)
	genre_sel_mem(integer)
	genre_sel_mytho(integer)
	genre_sel_mem_nos(integer)
	genre_sel_mem_hist(integer)
	genre_sel_mem_spri(integer)
	genre_sel_mytho_greek(integer)
	genre_sel_mytho_india(integer)
	action(integer)

goal
	makewindow(1,7,7,"BOOK RECOMMENDER SYSTEM ",0,0,25,80),
        repeat.

clauses	

repeat :-
    clearwindow,
    write("Q1. Are you a  1. Knee-high to a grass-hoper  2. Young blood  3. Not so Strong on your feet ? "),
    readint(Age),
    age_group(Age),
    write(" Enter 0 to end and 1 to continue  :  \n"),
    readint(Int),nl,
    action(Int).

action(0):-!,
exit.

action(1):-
repeat.

age_group(1):-
write("What do you like the most  ?\n"),
write("1. Comic strips of newspapers  2. Imaginary creatures and magic  3. Topping in class ? "),
readint(Genre_child),nl,
genre_c(Genre_child).

age_group(2):-
write("Are you interested in 1. Classic Literature  2. Reading other people lives   3. News with illustrations  :\n"),
write("Select a Genre :  "),
readint(Genre_youth),nl,
genre_y(Genre_youth).

age_group(3):-
write("What would you like to read about? \n : 1. Memoirs  2. Mythologies :\n"),
readint(Genre_old),nl,
genre_o(Genre_old).

	

genre_c(1):-
write("What kind of stories interest you ? \n"),
write("1. About superpowers  2. Crimes and detectives  3. Fictional world of science \n"),
readint(Choice),nl,
genre_sel_c(Choice).

genre_c(2):-
write("What kind of stories interest you ? \n"),
write("1. About Princesses   2. Magical powers   3. Moral Science stories  \n"),
readint(Choice),nl,
genre_sel_f(Choice).

genre_c(3):-
write("What topic are you interested in studying ? \n"),
write("1. Mathematics   2. Chemistry   3. Biology  \n"),
readint(Choice),nl,
genre_sel_a(Choice).



genre_sel_c(1):-
write("What superpower you would like to have ? \n"),
write("1. Superhuman strength plus wealth  2. Power of flying and X-ray vision  3. Mutated abilities  \n"),
readint(Super),nl,
genre_sel_c_super(Super).

genre_sel_c(2):-
write("How do you like to solve a crime  ? \n"),
write("1. With  a group of friends   2. Alone and using forensic sciences   3. Using Magical Powers  \n"),
readint(Crime),nl,
genre_sel_c_crime(Crime).

genre_sel_c(3):-
write("What are you most inquisitive about  ? \n"),
write("1. Humans and Aliens  2. Cyber Space , the Computer world   3. Journey through Space and Time  \n"),
readint(Sci),nl,
genre_sel_c_scifi(Sci).


genre_sel_f(1):-
write("What are you most interested in ? \n"),
write("1. Beauty   2. Long Hair  3. Beautiful Shoes  \n"),
readint(Pri),nl,
genre_sel_f_pri(Pri).

genre_sel_f(2):-
write("What are you most interested in ? \n"),
write("1. Dwarf   2. Genies  \n"),
readint(Magic),nl,
genre_sel_f_magic(Magic).

genre_sel_f(3):-
write("What do you like the most ? \n"),
write("1. Slow and steady wins the race   2. Unity is strength  \n"),
readint(Mor),nl,
genre_sel_f_moral(Mor).


genre_sel_a(1):-
write("Which standard are you in? \n"),
write("1. 10th   2. 12th  3. Graduation  \n"),
readint(Acad),nl,
genre_sel_a_math(Acad).

genre_sel_a(2):-
write("Which standard are you in? \n"),
write("1. 10th   2. 12th  3. Gradutation  \n"),
readint(Acad),nl,
genre_sel_a_chem(Acad).

genre_sel_a(3):-
write("Which standard are you in? \n"),
write("1. 10th   2. 12th  3. Gradutation  \n"),
readint(Acad),nl,
genre_sel_a_bio(Acad).



genre_sel_c_super(1):-
write("We recommend you Batman: The Dark Knight Returns and Justice League \n "),nl,nl.
genre_sel_c_super(2):-
write("We recommend you 1. SpiderMan : The venom  2. The Iron Man  \n "),nl,nl.
genre_sel_c_super(3):-
write("We recommend you X-men : The Uncanny Series  \n "),nl,nl.

genre_sel_c_crime(1):-
write("We recommend you the Secret Seven  and The Famous Five Series  \n "),nl,nl.
genre_sel_c_crime(2):-
write("We recommend you Sherlock Holmes by Sir Arthur Conan Doyle   \n "),nl,nl.
genre_sel_c_crime(3):-
write("We recommend you 1. Harry Potter series  2. Aladdin  Series   \n "),nl,nl.

genre_sel_c_scifi(1):-
write("We recommend you 1. Space Odyssey  2. Star Trek Series   \n "),nl,nl.
genre_sel_c_scifi(2):-
write("We recommend you 1. NeuroSciences  2. The War of the Computers    \n "),nl,nl.
genre_sel_c_scifi(3):-
write("We recommend you 1. Guide to the Galaxy   2. Toys in Space    \n "),nl,nl.


genre_sel_f_pri(1):-
write("We recommend you Beauty and the Beast by Gabrielle Suzanne Barbot de Villeneuve \n "),nl,nl.
genre_sel_f_pri(2):-
write("We recommend you Rapunzel by Brothers Grimm \n "),nl,nl.
genre_sel_f_pri(3):-
write("We recommend you Cinderella: Tale by Brothers Grimm and Giambattista Basile \n "),nl,nl.

genre_sel_f_magic(1):-
write("We recommend you Alladin and the Wonderful Lamp \n "),nl,nl.
genre_sel_f_magic(2):-
write("We recommend you Snow White and the Seven Dwarfs  \n "),nl,nl.

genre_sel_f_moral(1):-
write("We recommend you Tortoise and the Hare by Janet Stevens\n "),nl,nl.
genre_sel_f_moral(2):-
write("We recommend you Three Sons and a Bundle of Sticks\n "),nl,nl.


genre_sel_a_math(1):-
write("We recommend you A Journey Through Genius by William Dunbam  \n "),nl,nl.
genre_sel_a_math(2):-
write("We recommend you Senior Secondary School Mathematics by R.S Agarwal  \n "),nl,nl.
genre_sel_a_math(3):-
write("We recommend you  MEI Structured Maths Second Edition: Foundations of Advanced Maths \n "),nl,nl.

genre_sel_a_chem(1):-
write("We recommend you Foundation Science Chemistry by A.K. Singh   \n "),nl,nl.
genre_sel_a_chem(2):-
write("We recommend you Conceptual Chemistry by S. Chand  \n "),nl,nl.
genre_sel_a_chem(3):-
write("We recommend you The Golden Book of Chemistry Experiments   \n "),nl,nl.

genre_sel_a_bio(1):-
write("We recommend you Kenneth R. Miller, J. S. Biology: Pearson Prentice Hall.	\n "),nl,nl.
genre_sel_a_bio(2):-
write("We recommend you Elementary Biology: A Trueman Publication   \n "),nl,nl.
genre_sel_a_bio(3):-
write("We recommend you Developmental Biology, 3RD EDITION Saunders College Publishing   \n "),nl,nl.



genre_y(1):-
write("What do you like reading about? \n"),
write("1. Mystery 2. Fantasy 3. Romance\n"),
readint(Choice),nl,
genre_sel_n(Choice).

genre_y(2):-
write("What is more prefered? \n"),
write("1.Auto-Biographies 2. Biographies  \n"),
readint(Choice),nl,
genre_sel_b(Choice).

genre_y(3):-
write("What type of magazines would you like to read? \n"),
write("1.Fashion   2.Sports   3.Gadgets \n"),
readint(Choice),nl,
genre_sel_m(Choice).



genre_sel_n(1):-
write("Which author do you prefer? \n"),
write("1. Agatha Christy  2. Dan Brown  \n"),
readint(Mys),nl,
genre_sel_n_mys(Mys).

genre_sel_n(2):-
write(" What do you like the most  ? \n"),
write("1. Adventure   2. Intense Poetry   3. Magic, family and friends  \n"),
readint(Fan),nl,
genre_sel_n_fan(Fan).

genre_sel_n(3):-
write("What kind of love stories do you like to read  ? \n"),
write("1. Stories having moral sensability  2. Based on true story  3. Tragic love story  \n"),
readint(Rom),nl,
genre_sel_n_rom(Rom).


genre_sel_b(1):-
write("Which topic do you like among these? \n"),
write("1. Mathematics   2. Politics  3. Music  \n"),
readint(Ab),nl,
genre_sel_b_autobio(Ab).

genre_sel_b(2):-
write("What are you most interested in ? \n"),
write("1. Computers   2. Physics  3. Leadership  \n"),
readint(B),nl,
genre_sel_b_bio(B).

genre_sel_m(1):-
write("1. Mens Fashion   2. Womens Fashion  3. Kids Fashion  \n"),
readint(Fash),nl,
genre_sel_m_fash(Fash).


genre_sel_m(2):-
write("Which sport do you like to play? \n"),
write("1. Cricket 2. BasketBall 3. Footbal\n"),
readint(Spor),nl,
genre_sel_m_spor(Spor).

genre_sel_m(3):-
write("Which gadgets are you interested in? \n"),
write("1. Mobile   2. Laptops  3. Home Automation  \n"),
readint(Gadg),nl,
genre_sel_m_gad(Gadg).



genre_sel_n_mys(1):-
write("We recommend you Peril At End House \n "),nl,nl.
genre_sel_n_mys(2):-
write("We recommend you Da Vinci Code\n "),nl,nl.
genre_sel_n_fan(1):-
write("We recommend you Hobbit  \n "),nl,nl.
genre_sel_n_fan(2):-
write("We recommend you The lord Of The Rings\n "),nl,nl.
genre_sel_n_fan(3):-
write("We recommend you Harry Potter Series\n "),nl,nl.

genre_sel_n_rom(1):-
write("We recommend you Jane Eyre by Charlotte Bronte  \n "),nl,nl.
genre_sel_n_rom(2):-
write("We recommend you The Notebook by Nicholas \n "),nl,nl.
genre_sel_n_rom(3):-
write("We recommend you P.S. I Love You  \n "),nl,nl.


genre_sel_b_autobio(1):-
write("We recommend you I Am A Mathematician: Nobert Wiener \n "),nl,nl.
genre_sel_b_autobio(2):-
write("We recommend you Mein Kampf : Adolf Hitler\n "),nl,nl.
genre_sel_b_autobio(3):-
write("We recommend you The Way I Am: Enimen\n "),nl,nl.

genre_sel_b_bio(1):-
write("We recommend you Steve Jobs: A Biography\n "),nl,nl.
genre_sel_b_bio(2):-
write("We recommend you Einstein : His Life and Universe \n "),nl,nl.
genre_sel_b_bio(3):-
write("We recommend you Wings Of Fire: APJ Abdul Kalam\n "),nl,nl.

genre_sel_m_fash(1):-
write("We recommend you GQ Style Magazine  \n "),nl,nl.
genre_sel_m_fash(2):-
write("We recommend you 1. Marie Claire  2. Cosmopolitian  \n "),nl,nl.
genre_sel_m_fash(3):-
write("We recommend you 1. Junior  2. Bella Child  \n "),nl,nl.

genre_sel_m_spor(1):-
write("We recommend you 1. Cricket Today  2. AllOut Cricket  \n "),nl,nl.
genre_sel_m_spor(2):-
write("We recommend you 1. Slam  2. Time \n "),nl,nl.
genre_sel_m_spor(3):-
write("We recommend you 1. 90 Mins  2. Footy Focus \n "),nl,nl.

genre_sel_m_gad(1):-
write("We recommend you 1.Mobile Choice  2. Stuff- The Android\n "),nl,nl.
genre_sel_m_gad(2):-
write("We recommend you What-Laptop magazine  \n "),nl,nl.
genre_sel_m_gad(3):-
write("We recommend you 1. Smart-Home  2. Automation  \n "),nl,nl.


genre_o(1):-
write("What type of memoirs interest you? \n"),
write("1. Nostalgia 2. History and Politics 3. Spirituality\n"),
readint(Choice),nl,
genre_sel_mem(Choice).

genre_o(2):-
write("Which mythologies do you like reading about? \n"),
write("1.Greek Mythology 2.Indian Mythology \n"),
readint(Choice),nl,
genre_sel_mytho(Choice).


genre_sel_mem(1):-
write("What type of stories are you interested in? \n"),
write("1. Tragedies in life  2. About Family and Tradition  \n"),
readint(Nos),nl,
genre_sel_mem_nos(Nos).

genre_sel_mem(2):-
write(" What topic are you interested in reading about? \n"),
write("1. The Audacity of Hope  2. Political Genius\n"),
readint(Hist),nl,
genre_sel_mem_hist(Hist).

genre_sel_mem(3):-
write("What topic are you interested in reading about? \n"),
write("1.Courage 2. Thoughts on Faith \n"),
readint(Spri),nl,
genre_sel_mem_spri(Spri).


genre_sel_mytho(1):-
write("What type of stories are you interested in? \n"),
write("1. Ware between Greeks and Trojans 2. About Half man Half God  \n"),
readint(Greek),nl,
genre_sel_mytho_greek(Greek).

genre_sel_mytho(2):-
write(" What topic are you interested in reading about? \n"),
write("1. The Shiva  2. The victory of Good over Evil\n"),
readint(India),nl,
genre_sel_mytho_india(India).



genre_sel_mem_nos(1):-
write("We recommend you Rachmaninoff's Cape \n "),nl,nl.
genre_sel_mem_nos(2):-
write("We recommend you Millie's Notes And Nostalgia \n "),nl,nl.
genre_sel_mem_hist(1):-
write("We recommend you The Audacity Of Hope: Obama  \n "),nl,nl.
genre_sel_mem_hist(2):-
write("We recommend you The Tean Of Rivals: Abrahmin Lincoln\n "),nl,nl.
genre_sel_mem_spri(1):-
write("We recommend you Girl Meets God\n "),nl,nl.

genre_sel_mem_spri(2):-
write("We recommend you 1. Travelling Mercies  2. Plan B \n "),nl,nl.
genre_sel_mytho_greek(1):-
write("We recommend you The LLiads and Odyssey \n "),nl,nl.
genre_sel_mytho_greek(2):-
write("We recommend you Percy Jackson Series  \n "),nl,nl.


genre_sel_mytho_india(1):-
write("We recommend you The Shiva Triogy\n "),nl,nl.
genre_sel_mytho_india(2):-
write("We recommend you Tales Of Ramayana \n "),nl,nl.

