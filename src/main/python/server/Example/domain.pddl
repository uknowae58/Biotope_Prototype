
(define 
    (domain demoDomain)
    (:requirements :typing :strips :negative-preconditions :conditional-effects :universal-preconditions :equality :fluents :disjunctive-preconditions)

    (:types
        ort - object
        parkplatz-id - object
        elektroParkplatzId - parkplatz-id
        restaurant-id - object
        tisch - object
    )

    (:predicates
        (parkplatz-ist-an-ort ?p - parkplatz-id ?o - ort)
        (restaurant-ist-an-ort ?r - restaurant-id ?o - ort)
        (parkplatz-gebucht ?p - parkplatz-id)
        (waschen-gebucht ?p - parkplatz-id)
        (tisch-ist-in-restaurant ?t - tisch ?r - restaurant-id)
        (tisch-gebucht ?t - tisch)
)

    (:action post_reserviere-parkplatz
        :parameters (
            ?p - parkplatz-id
        )
        :precondition (and
            (not (parkplatz-gebucht ?p) )
        )
        :effect (and
                (parkplatz-gebucht ?p)
            )
    )
    
    (:action post_buche-waschen
        :parameters (
            ?p - parkplatz-id
        )
        :precondition ( and
            (parkplatz-gebucht ?p)
            (forall (?p1 - elektroParkplatzId)
                (not (= ?p ?p1))
            )
        )
        :effect (and
            (waschen-gebucht ?p)
        )
    )
    
    ;interne aktion zur kontrolle, dass die ergebnisse (zwischenschritte) auch erreicht sind
    (:action get_ist-parkplatz-frei-an-ort_intern
        :parameters (
            ?o - ort
            ?p - parkplatz-id
        )
        :precondition (and
            (not (parkplatz-gebucht ?p))
            (forall (?x - ort)( and
                (not (parkplatz-ist-an-ort ?p ?x))
            ))
        )
        :effect (and
                (parkplatz-ist-an-ort ?p ?o)
         )
    )

    ; Was ich Möchte:
    ; Ich möchte einen Paltz im Restaurant buchen können auch ohne Parkplatz
    ; Ich möchete die Möglichkeit haben, einen Platz im Restaurant zu buchen, wenn ich einen Parkplatz bekommen kann. 

    (:action restaurant-ist-an-ort_intern
        :parameters (
            ?r - restaurant-id
            ?o - ort
        )
        :precondition (and
                (forall (?x - ort)(and
                    (not (restaurant-ist-an-ort ?r ?x))
                ))
        )
        :effect (and
            (restaurant-ist-an-ort ?r ?o)
         )
    )

    (:action tisch-ist-in-restaurant_intern
        :parameters (
            ?t - tisch
            ?r - restaurant-id
        )
        :precondition (and
                (forall (?x - restaurant-id)(and
                    (not (tisch-ist-in-restaurant ?t ?x))
                ))
                (exists (?o - ort)
                    (restaurant-ist-an-ort ?r ?o ))
        )
        :effect (and
            (tisch-ist-in-restaurant ?t ?r)
         )
    )

    (:action post-tisch-buchen
        :parameters (
            ?t - tisch
        )
        :precondition (and
                (exists (?r - restaurant-id)
                    (tisch-ist-in-restaurant ?t ?r))
                (not (tisch-gebucht ?t))
        )
        :effect (and
            (tisch-gebucht ?t)
         )
    )
)