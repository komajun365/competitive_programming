g++ a.cpp
for infile in $( ls ../input ); do
	bname=`basename $infile`
	inname=${bname%.*}
	outfilename=../output/$inname.out
	echo ../input/$infile to $outfilename
	./a.out < ../input/$infile > $outfilename
done
