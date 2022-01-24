(define (square x) (* x x))

(define (pow x y)
 (if (= y 1) x 
	(if (odd? y) (* x (square (pow x (quotient (- y 1) 2))))
		(square (pow x (quotient y 2)))
	)
 )
)
