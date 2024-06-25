% Define diseases and their associated symptoms
disease(cold) :- symptom(fever), symptom(cough), symptom(sore_throat), symptom(runny_nose).
disease(flu) :- symptom(fever), symptom(headache), symptom(cough), symptom(sore_throat), symptom(runny_nose), symptom(body_ache).
disease(covid19) :- symptom(fever), symptom(cough), symptom(shortness_of_breath), symptom(loss_of_taste), symptom(loss_of_smell).
disease(allergy) :- symptom(runny_nose), symptom(sneezing), symptom(itchy_eyes).

% Define symptoms
symptom(fever).
symptom(cough).
symptom(sore_throat).
symptom(runny_nose).
symptom(headache).
symptom(body_ache).
symptom(shortness_of_breath).
symptom(loss_of_taste).
symptom(loss_of_smell).
symptom(sneezing).
symptom(itchy_eyes).

% Diagnosis based on symptoms
diagnose(Disease) :-
    disease(Disease),
    write('The diagnosis is: '), write(Disease), nl.

% Asking for symptoms from the user
ask_symptoms :-
    write('Do you have fever? (yes/no) '), read(Ans1), process_answer(fever, Ans1),
    write('Do you have cough? (yes/no) '), read(Ans2), process_answer(cough, Ans2),
    write('Do you have sore throat? (yes/no) '), read(Ans3), process_answer(sore_throat, Ans3),
    write('Do you have runny nose? (yes/no) '), read(Ans4), process_answer(runny_nose, Ans4),
    write('Do you have headache? (yes/no) '), read(Ans5), process_answer(headache, Ans5),
    write('Do you have body ache? (yes/no) '), read(Ans6), process_answer(body_ache, Ans6),
    write('Do you have shortness of breath? (yes/no) '), read(Ans7), process_answer(shortness_of_breath, Ans7),
    write('Do you have loss of taste? (yes/no) '), read(Ans8), process_answer(loss_of_taste, Ans8),
    write('Do you have loss of smell? (yes/no) '), read(Ans9), process_answer(loss_of_smell, Ans9),
    write('Do you have sneezing? (yes/no) '), read(Ans10), process_answer(sneezing, Ans10),
    write('Do you have itchy eyes? (yes/no) '), read(Ans11), process_answer(itchy_eyes, Ans11),
    diagnose(Disease),
    write('Possible disease: '), write(Disease), nl.

% Process user answers to symptoms
process_answer(Symptom, yes) :- assert(symptom(Symptom)).
process_answer(Symptom, no) :- retractall(symptom(Symptom)).

% Run the medical diagnosis system
run_diagnosis :-
    retractall(symptom(_)),
    ask_symptoms.

% Example query to start the diagnosis:
% ?- run_diagnosis.
