(define 
    (problem demoName)
    (:domain demoDomain)
    (:objects
        o1 - ort
t1 - tisch
r1 - restaurant-id

    )
    (:init
        (restaurant-ist-an-ort r1 o1)
    )

    (:goal
        (and (tisch-gebucht t1) (tisch-ist-in-restaurant t1 r1))
    )
)