#include <iostream>
#include <vector>
using namespace std;

void pass_by_value(int a){
	a = 6;
	return;
}

void pass_by_reference(int& b){
	b = 6;
	return;
}

int next_in_array(int arr[]){
	// cout << "[next_in_array]" << arr+1 << endl;
	int nxt = *(arr + 1);
	/* (Cannot use `int& nxt = arr + 1;`, since arr is a temp ref. One cannot bind a temp ref to a const.)
	p_by_value_ref.cpp:15:7: error: non-const lvalue reference to type 'int' cannot bind to a temporary of
      type 'int *'
        int& nxt = arr + 1;
             ^     ~~~~~~~
	1 error generated.
	*/
	*(arr+1) = 100;
	return nxt;
}

void p_array(int arr[], int size){
	for(int i=0; i<size; i++){
		cout << arr[i] << ",";
	}
	cout << endl;
}

void mod_vector1(vector<int> vect){
	vect[0] = 101;
}

void mod_vector2(vector<int>& vect){
	vect[0] = 101;
}

void p_vect(vector<int>& vect){
	for(int i=0; i<vect.size(); i++){
		cout << vect[i] << ",";
	}
	cout << endl;
}

int main() {
	// value
	int a = 1;
	int b = 1;
	pass_by_value(a);
	pass_by_reference(b);
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;

	// array
	int arr [4] = {1,3,5,7};
	cout << "array_next = " << next_in_array(arr) << endl;
	cout << "arr = ";
	p_array(arr, sizeof(arr)/sizeof(arr[0]));

	// vector
	vector<int> vect1{1,3,5,7};
	vector<int> vect2{1,3,5,7};
	mod_vector1(vect1);
	mod_vector2(vect2);

	cout << "vect1 = ";
	p_vect(vect1);
	cout << "vect2 = ";
	p_vect(vect2);
	
	return 0;

	/*
	a = 1
	b = 6
	array_next = 3
	arr = 1,100,5,7,
	vect1 = 1,3,5,7,
	vect2 = 101,3,5,7,
	*/
}