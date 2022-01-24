(define (replicate x n)
	(define (rep_help x n s)
		(if (= n 0) s
			(rep_help x (- n 1) (cons x s))
		)
	)
	(rep_help x n `())
)
