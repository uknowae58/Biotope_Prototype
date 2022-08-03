(define 
    (problem parkPlatzBuchenUndWaschenTypHierachie)
    (:domain demoDomain)
    (:objects
        o1 - ort
        t1 - tisch
        r1 - restaurant-id)
    (:init)

    (:goal
        (and 
            (tisch-gebucht t1) 
            (tisch-ist-in-restaurant t1 r1))
    )
)

0.0: (restaurant-ist-an-ort_intern r1 o1)
