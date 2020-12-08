# RPi_IoT_Battleship_SenseHat
Raspberry Pi IoT application using Flask web app framework and SenseHat to build a Battleship game and display information from the RPi's SenseHat sensor to a webpage

Developed for the course "Διαδίκτυο των Πραγμάτων (IoT) στην Πράξη: με Raspberry Pi και Python (Νέο)" from https://mathesis.cup.gr/courses/course-v1:ComputerScience+CS4.1+20D/about

Δημιουργία παιχνιδιού "Ναυμαχίας" με χρήση του Flask και του Sense-HAT
Στην εργασία αυτή σας ζητείται να προσθέσετε περισσότερες δυνατότητες στο πρόγραμμα myapp.py. Μία από αυτές τις δυνατότητες είναι η δημιουργία μιας σελίδας που θα φιλοξενεί το παιχνίδι Ναυμαχία. Στην περίπτωση που δε διαθέτετε το Raspberry Pi, μπορείτε να χρησιμοποιήσετε το sense-hat emulator και το Raspberry Pi OS Desktop σε εικονικό μηχάνημα (VM).

Περιγραφή:
Αρχικά, στο αρχείο myapp.py θα πρέπει να γίνει η κατάλληλη αλλαγή, ώστε κατά την εκκίνησή του, να σβήνουν όλα τα LED της συστοιχίας.

Δημιουργήσετε την αρχική σελίδα index.html η οποία θα αντιστοιχεί στη διαδρομή ('/'). Θα πρέπει στο αρχείο myapp.py να γίνουν οι απαραίτητες αλλαγές, ώστε μόλις ο χρήστης δώσει τον κωδικό του, να πλοηγηθεί αυτόματα στην αρχική σελίδα index.html. Η σελίδα αυτή θα περιλαμβάνει το χαιρετισμό του χρήστη, όπως στη σελίδα info.html, καθώς και τρεις συνδέσμους. Ο πρώτος σύνδεσμος με όνομα Δεδομένα αισθητήρων, θα οδηγεί τον χρήστη στη διεύθυνση /sense. O δεύτερος σύνδεσμος με όνομα Ναυμαχία θα οδηγεί τον χρήστη στη διεύθυνση /ships που θα αναλύσουμε παρακάτω. Τέλος ο σύνδεσμος Αποσύνδεση θα οδηγεί τον χρήστη στη διεύθυνση /logme. Φροντίστε να μην επιτρέπεται η πρόσβαση στην αρχική σελίδα αν ο επισκέπτης δεν έχει συνδεθεί με τον κωδικό του, όπως δηλαδή έχουμε φροντίσει και για τη σελίδα /sense.

Ο χρήστης, αφού πλοηγηθεί στη διεύθυνση /sense, εκτός από τη θερμοκρασία και υγρασία, θα λαμβάνει και την τιμή βαρομετρικής πίεσης με ακρίβεια τριών δεκαδικών ψηφίων. Στο τέλος της ίδιας σελίδας θα πρέπει να αλλάξει ο σύνδεσμος Αποσύνδεση σε Αρχική σελίδα ο οποίος θα οδηγεί στη σελίδα index.html που θα δημιουργήσουμε.

Τέλος αναπτύξετε το παιχνίδι ναυμαχία, το οποίο θα εκτυλίσσεται πάνω στη συστοιχία LED. Για το σκοπό αυτό, θα πρέπει να δημιουργήσετε νέα σελίδα ships.html και διαδρομή με όνομα /ships όπου θα φιλοξενηθεί μια απλή εκδοχή του παιχνιδιού.
Η σελίδα αυτή εκτός από το χαιρετισμό του χρήστη, θα περιλαμβάνει δύο πεδία για την επιλογή θέσης του LED που θέλουμε να ενεργοποιήσουμε, ένα κουμπί με όνομα ΑΠΟΣΤΟΛΗ στο Sense-HAT για την αποστολή των δεδομένων, ένα σύνδεσμο με όνομα Ανανέωση που θα οδηγεί στη σελίδα που βρισκόμαστε ώστε να την ανανεώνει και το σύνδεσμο Αρχική σελίδα που θα οδηγεί στη σελίδα index.html. Το πρώτο από τα δύο πεδία αντιστοιχεί στον οριζόντιο άξονα, ενώ το δεύτερο αντιστοιχεί στον κάθετο άξονα και οι δυνατές τιμές για κάθε πεδίο είναι από το 0, το οποίο αντιστοιχεί στο πρώτο LED του άξονα, μέχρι το 7 το οποίο αντιστοιχεί στο όγδοο στοιχείο του άξονα. Ο χρήστης θα πρέπει να έχει τη δυνατότητα να χρωματίσει με μπλε χρώμα[0,0,200] το αντίστοιχο LED που θα επιλέξει. Για παράδειγμα αν θέλει να χρωματίσει το δεύτερο LED της πρώτης γραμμής, θα πρέπει να δώσει στο πρώτο πεδίο τον αριθμό 1, στο δεύτερο το 0 και να πατήσει το κουμπί ΑΠΟΣΤΟΛΗ στο Sense-HAT.
Όταν ο χρήστης επιλέγει αριθμό μεγαλύτερο του 7 στο πρώτο πεδίο και οποιοδήποτε ακέραιο στο δεύτερο πεδίο, θα σβήνουν όλα τα LED της συστοιχίας, ενώ θα ενεργοποιούνται σε 10 τυχαίες θέσεις της συστοιχίας LED τα πλοία με πράσινο χρώμα[0,200,0]. Φροντίστε κάθε φορά να αλλάζουν οι θέσεις αυτές.
Σε αυτή την απλή εκδοχή της ναυμαχίας δεν είναι απαραίτητο να ελέγχουμε ότι έχουν εμφανιστεί τα πλοία πριν ο χρήστης ξεκινήσει να χρωματίζει τα LED. Επίσης ο λόγος που πρέπει να συμπληρωθεί και το 2ο πεδίο είναι διότι σε αυτή την απλή εκδοχή της εφαρμογής δεν είναι απαραίτητος ο αμυντικός προγραμματισμός. Φροντίστε να μην επιτρέπεται η πρόσβαση στη σελίδα /ships αν ο επισκέπτης δεν έχει συνδεθεί με τον κωδικό του.

Διευκρινίσεις υλοποίησης:
Για την υλοποίηση της ναυμαχίας θα χρησιμοποιήσετε τις παρακάτω εντολές οι οποίες θα πρέπει να συμπεριληφθούν στην αρχή του myapp.py:


import random # Εισάγουμε τη βιβλιοθήκη random.
green=[0,200,0] # Για τις θέσεις των στόχων χρησιμοποιούμε το πράσινο χρώμα,
black=[0,0,0]   # ενώ κανένα χρώμα για τις υπόλοιπες θέσεις. 
# Δημιουργούμε τη λίστα μεγέθους 64 στοιχείων
# που περιλαμβάνουν 10 θέσεις-στόχους:
shipmap=[green]*10+[black]*54 
Τοποθετούμε την παρακάτω εντολή στο σημείο που θα πρέπει να αλλάξει η σειρά των στοιχείων της παραπάνω λίστας, ώστε να αναμειχθούν και οι στόχοι:

random.shuffle(shipmap)
Μετά τη random.shuffle() εμφανίζουμε τη λίστα shipmap στη συστοιχία LED με χρήση της κατάλληλης εντολής όπως έχουμε μάθει.

Για να χρωματίσουμε ένα συγκεκριμένο LED της συστοιχίας, θα χρησιμοποιήσουμε τη συνάρτηση set_pixel(), η οποία συντάσσεται ως εξής:

set_pixel(x,y,[r,g,b])
Το όρισμα x είναι η τιμή στον οριζόντιο άξονα, το y η τιμή στον κάθετο άξονα, και τα επόμενα τρία ορίσματα αφορούν το χρώμα [r=red, g=green, b=blue]. Για το μπλε χρώμα συντάσσουμε την εντολή ως set_pixel(x,y,[0,0,200]).

Στην άσκηση αυτή δεν απαιτείται η χρήση αμυντικού προγραμματισμού για να να ελεγχθεί η ορθότητα των δεδομένων του χρήστη. Συνεπώς, προκειμένου η εφαρμογή να δουλέψει χωρίς σφάλματα, θα πρέπει ο χρήστης να συμπληρώνει όλα τα πεδία με ακέραιες αριθμητικές τιμές.

Ζητούμενα και βαθμολογία εργασίας:
Κατά την εκκίνηση της εφαρμογής θα πρέπει να σβήνουν όλα τα τυχόν ενεργά LED της συστοιχίας (10 %).
Δημιουργία νέας σελίδας index.html και αντιστοίχισή της στη διαδρομή ('/'). Αυτή η σελίδα θα περιλαμβάνει το μήνυμα καλωσορίσματος στον χρήστη όπως εμφανίζεται στη σελίδα info.html. Επίσης θα περιλαμβάνει τους συνδέσμους Δεδομένα αισθητήρων, Ναυμαχία και Αποσύνδεση. Ο πρώτος σύνδεσμος με όνομα Δεδομένα αισθητήρων θα οδηγεί τον χρήστη στη διεύθυνση /sense. O δεύτερος σύνδεσμος με όνομα Ναυμαχία θα οδηγεί τον χρήστη στη διεύθυνση /ships και ο σύνδεσμος Αποσύνδεση θα οδηγεί τον επισκέπτη στη διεύθυνση /logme (25 %).
Εμφάνιση βαρομετρικής πίεσης στη σελίδα /sense με ακρίβεια τριών δεκαδικών ψηφίων. Αλλαγή του συνδέσμου Αποσύνδεση σε Αρχική σελίδα, ο οποίος θα οδηγεί στη σελίδα index.html (20 %).
Δημιουργία νέας σελίδας ships.html και διαδρομής με όνομα /ships, η οποία θα περιλαμβάνει το μήνυμα καλωσορίσματος στον χρήστη, δύο πεδία για τη συμπλήρωση των συντεταγμένων της θέσης του LED, καθώς επίσης το κουμπί ΑΠΟΣΤΟΛΗ στο sense-HAT και τους συνδέσμους Αρχική σελίδα και Ανανέωση. Όταν ο χρήστης πατήσει το κουμπί ΑΠΟΣΤΟΛΗ στο sense-HAT θα πρέπει να ενεργοποιηθεί με το κατάλληλο χρώμα το αντίστοιχο LED στη συστοιχία (25 %).
Να γίνουν οι απαραίτητες ενέργειες στο πρόγραμμα, ώστε αν ο χρήστης δώσει αριθμό άνω του 7 στο πρώτο πεδίο που αντιπροσωπεύει τον οριζόντιο άξονα, να αρχικοποιείται η συστοιχία LED, ενεργοποιώντας σε τυχαία θέση μόνο τα 10 πράσινα LED, τα οποία αντιπροσωπεύουν τα πλοία (10 %).
Να γίνουν οι απαραίτητες ενέργειες, ώστε να μην επιτρέπεται η πρόσβαση στην αρχική σελίδα, στη σελίδα της ναυμαχίας και στη σελίδα /sense, αν ο χρήστης δεν έχει συνδεθεί με τον κωδικό του (10 %).
Για τη βαθμολόγηση της εργασίας αυτής δε θα ληφθεί υπόψη ο τρόπος μορφοποίησης των σελίδων.

Προαιρετικά:
Αν υλοποιήσετε σωστά όλα τα ζητούμενα της περιγραφής που προηγήθηκε, θα λάβετε τον πλήρη βαθμό της εργασίας, ο οποίος αντιστοιχεί στο 55% του συνολικού βαθμού (45% εβδομαδιαία ΤΕΣΤ + 55% τελική εργασία).
Προαιρετικά για όσους θέλουν να πειραματιστούν περισσότερο, ή έχουν χάσει κάποια από τα ΤΕΣΤ και θέλουν να βελτιώσουν το βαθμό τους, δίνεται η δυνατότητα περαιτέρω ανάπτυξης του παιχνιδιού και απόκτησης bonus μέχρι και 10% πλέον του συνολικού βαθμού.
Στην περίπτωση αυτή, δημιουργήστε ένα αντίγραφο της σελίδας ships.html σε bonus_ships.html, με την αντίστοιχη διεύθυνση /bonus_ships και εφαρμόστε εκεί τις παρακάτω βελτιώσεις (μην παραλείψετε να προσθέσετε τον κατάλληλο σύνδεσμο στο index.html όπως και να ενημερώσετε το σύνδεσμο Ανανέωση μέσα στο bonus_ships.html):

Έλεγχος των τιμών που δίνει ο χρήστης με χρήση αμυντικού προγραμματισμού. Εμφάνιση σχετικού μηνύματος στον χρήστη, πχ "Λανθασμένη είσοδος, δοκιμάστε ξανά".
Η εφαρμογή να μην επιτρέπει στον παίκτη να ενεργοποιήσει οποιοδήποτε LED αν δεν υπάρχουν ενεργά πράσινα LED (πλοία) στη συστοιχία.
Προσθήκη και δεύτερου παίκτη ο οποίος θα εμφανίζει τις επιλεγμένες θέσεις στη συστοιχία LED με κόκκινο χρώμα[200,0,0]. Ο δεύτερος παίκτης θα μπορεί να συνδεθεί από άλλο υπολογιστή ή φυλλομετρητή, χρησιμοποιώντας διαφορετικά στοιχεία πρόσβασης από τον πρώτο. Η επιλογή του χρώματος που θα αντιστοιχεί σε κάθε χρήστη θα γίνεται σύμφωνα με το user_id. Δηλαδή αν το user_id του χρήστη είναι ζυγός αριθμός, ο χρήστης θα λάβει το κόκκινο χρώμα, ενώ ο χρήστης με μονό αριθμό στο user_id θα λάβει το μπλε χρώμα. Το χρώμα του χρήστη θα εμφανίζεται στην αρχή της σελίδας μετά το όνομά του. Η σειρά των παικτών δεν ελέγχεται.
Αν ο παίκτης με το μπλε χρώμα πετύχει πλοίο (πράσινο LED), τότε το χρώμα στη θέση αυτή θα γίνει [0,200,200], ενώ αν ο παίκτης με το κόκκινο χρώμα πετύχει πλοίο, τότε το χρώμα στη θέση αυτή θα γίνει [200,200,0].
Έλεγχος αν το LED που πρόκειται να επιλέξει ο παίκτης είναι ήδη ενεργό από τον ίδιο ή από τον άλλο παίκτη. Στην περίπτωση που είναι ήδη ενεργό, να εμφανιστεί σχετικό μήνυμα.
Όταν ο παίκτης εξαντλήσει το τελευταίο πράσινο LED, να ενημερωθεί μέσω μηνύματος στη σελίδα πως το παιχνίδι τελείωσε.
Καταμέτρηση των ενεργών LED ανά χρώμα και εμφάνιση των αποτελεσμάτων καθ' όλη τη διάρκεια του παιχνιδιού κάτω από το κουμπί ΑΠΟΣΤΟΛΗ στο Sense-HAT. Αυτά τα αποτελέσματα θα ενημερώνονται κάθε φορά που ο χρήστης ανανεώνει την σελίδα ή πατάει το κουμπί ΑΠΟΣΤΟΛΗ στο Sense-HAT. Για την καταμέτρηση των ενεργών LED θα βοηθήσει η συνάρτηση get_pixels() η οποία επιστρέφει μία λίστα εξήντα τεσσάρων (64) στοιχείων που αφορούν το χρώμα του κάθε LED.
Για να λάβετε ολόκληρο το bonus, θα πρέπει να έχετε ολοκληρώσει τουλάχιστον τα 6 από τα παραπάνω 7 ζητούμενα. Για κάθε ζητούμενο που ολοκληρώνετε θα λάβετε το 1/6 του bonus.

