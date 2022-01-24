(define (unique s) 
    (if (null? s) `() 
        (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
)
