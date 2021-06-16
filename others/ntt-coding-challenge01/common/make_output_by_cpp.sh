if [ $# -ne 1 ]; then
	echo "please select problem folder"
	exit 1
fi

g++ ../$1/cpp/$1.cpp

for file in `ls ../$1/gen_io/in`
do
	echo "in file = ../$1/gen_io/in/$file"
	echo "out file = ../$1/gen_io/out/${file%.*}.out"
	./a.out < ../$1/gen_io/in/$file > ../$1/gen_io/out/${file%.*}.out
done

rm a.out
