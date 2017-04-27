package unit


import (

	. "strings"

	"testing"

)


var compareTests = []struct {

	a, b string

	i    int

}
func TestCompare(t *testing.T) {

	for _, tt := range compareTests {

		cmp := Compare(tt.a, tt.b)

		if cmp != tt.i {

			t.Errorf(`Compare(%q, %q) = %v`, tt.a, tt.b, cmp)

		}

	}

}


func TestCompareIdenticalString(t *testing.T) {

	var s = "Hello Gophers!"

	if Compare(s, s) != 0 {

		t.Error("s != s")

	}

	if Compare(s, s[:1]) != 1 {

		t.Error("s > s[:1] failed")

	}

}
 
