(define 
    (problem parkPlatzBuchenUndWaschenTypHierachie)
    (:domain demoDomain)
    (:objects
        o1 - ort
        p1 - parkplatz-id)
    (:init
        (parkplatz-ist-an-ort p1 o1))

    (:goal
        (and (
            (parkplatz-gebucht p1) 
            (waschen-gebucht p1))
    )
)