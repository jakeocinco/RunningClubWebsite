(define mult
  (lambda (x y z)
    (* (* x y) z)
  )
)


(define succ
  (lambda (n lst max)
    (define lst2 (append lst (list n)))
    (if (= n max)
        lst2
        (succ (+ n 1) lst2 max))))


(define filter-mults
  (lambda (lst lst2 y)
    (if (null? lst)
        lst2
        (if (= (modulo (car lst) y ) 0)
            (filter-mults (cdr lst) lst2 y)
            (filter-mults (cdr lst) (append lst2 (list (car lst))) y)
        )
    )
  )
)


(define sieve
  (lambda (lst lstWhole)
    (if (null? (cdr lst))
        lstWhole
        (sieve (filter-mults (cdr lst) '() (car lst)) (append lstWhole (list (car lst))))
    )
  )
)

(define get-primes
  (lambda (n)
         (if (= n 0)
             '()
             (sieve (succ 2 '() n) '())
        )
   )
)
