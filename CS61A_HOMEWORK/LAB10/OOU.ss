(define (over-or-under num1 num2)
 (cond((< num1 num2) -1)
	  ((eqv? num1 num2) 0)
	  ((> num1 num2) 1))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0
