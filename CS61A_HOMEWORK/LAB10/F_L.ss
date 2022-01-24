(define (filter-lst fn lst)
	(if (null? lst) nil
		(if (fn (car lst))
			(cons (car lst) (filter-lst fn (cdr lst)))
			(filter-lst fn (cdr lst))
		)
	)
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)
