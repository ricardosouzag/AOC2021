import System.IO  
import Control.Monad

main = do  
        contents <- readFile "day2.txt"
        let input = words contents
        let instructions = combineInstructions input
        let coords1 = applyInstructions1 instructions (0,0)
        print $ (product . pairToList) coords1
        let coords2 = applyInstructions2 instructions (0,0,0)
        print $ (product . pairToList . dropThird) coords2


pairToList :: (a,a) -> [a]
pairToList (x,y) = [x,y]

dropThird :: (a,b,c) -> (a,b)
dropThird (x,y,z) = (x,y)


readInt :: String -> Int
readInt = read

combineInstructions :: [String] -> [(Char, Int)]
combineInstructions [str, n]    = [(head str, readInt n)]
combineInstructions (str:n:rest) = (head str, readInt n) : combineInstructions rest

applyInstructions1 :: [(Char, Int)] -> (Int, Int) -> (Int, Int)
applyInstructions1 [(ch, n)] (p, d)     | ch == 'f' = (p + n, d) 
                                        | ch == 'd' = (p, d + n)
                                        | otherwise = (p, d - n)
applyInstructions1 (i:rest) (p, d)      = applyInstructions1 rest (applyInstructions1 [i] (p, d))

applyInstructions2 :: [(Char, Int)] -> (Int, Int, Int) -> (Int, Int, Int)
applyInstructions2 [(ch, n)] (p, d, a)  | ch == 'f' = (p + n, d + (n * a), a)
                                        | ch == 'd' = (p, d, a + n)
                                        | otherwise = (p, d, a - n)
applyInstructions2 (i:rest) (p, d, a)   = applyInstructions2 rest (applyInstructions2 [i] (p, d, a))
