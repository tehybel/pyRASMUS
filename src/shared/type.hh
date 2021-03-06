// -*- mode: c++; tab-width: 4; indent-tabs-mode: t; eval: (progn (c-set-style "stroustrup") (c-set-offset 'innamespace 0) (c-set-offset 'inextern-lang 0)); -*-
// vi:set ts=4 sts=4 sw=4 noet :
// Copyright 2014 The pyRASMUS development team
// 
// This file is part of pyRASMUS.
// 
// pyRASMUS is free software: you can redistribute it and/or modify it under
// the terms of the GNU Lesser General Public License as published by the
// Free Software Foundation, either version 3 of the License, or (at your
// option) any later version.
// 
// pyRASMUS is distributed in the hope that it will be useful, but WITHOUT ANY
// WARRANTY; without even the implied warranty of MERCHANTABILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
// License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with pyRASMUS.  If not, see <http://www.gnu.org/licenses/>
#ifndef __type_hh__
#define __type_hh__
#include <cstdint>
#include <ostream>

enum class LType: std::uint16_t {
	smallText, concatText, substrText, canonicalText, function
};

enum Type {
	TBool=0,
	TInt=1,
	TText,
	TRel,
	TTup,
	TFunc,
	TInvalid,
	TAny,
	TAtom,
	TNAMEQ,
};

inline const char * typeName(Type t) {
	switch(t) {
	case TBool: return "TBool";
	case TInt: return "TInt";
	case TInvalid: return "TInvalid";
	case TText: return "TText";
	case TRel: return "TRel";
	case TTup: return "TTup";
	case TFunc: return "TFunc";
	case TAny: return "TAny";
	case TAtom: return "TAtom";
	case TNAMEQ: return "TNAMEQ";
	}
}

inline std::ostream & operator<<(std::ostream & o, Type t) {
	return o << typeName(t);
}

#endif //__type_hh__
