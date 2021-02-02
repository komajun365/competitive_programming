if [ $# -ne 2 ]; then
	echo "please select problem folder or python script"
	exit 1
fi

g++ ../$1/cpp/$1.cpp

for file in `ls ../$1/gen_io/in`
do
	echo $file
	./a.out < ../$1/gen_io/in/$file > ./testcpp.out
	python3 ../$1/python/$2 < ../$1/gen_io/in/$file  > ./testpython.out
	diff ./testcpp.out ./testpython.out
done

rm a.out
rm ./testpython.out
rm ./testcpp.out
