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
#ifndef __parser_hh__
#define  __parser_hh__

#include <frontend/lexer.hh>
#include <frontend/error.hh>
#include <frontend/AST.hh>
#include <memory>

class IncompleteInputException: public std::exception {
public:
};

class Parser {
public:
	virtual ~Parser() {};
	virtual NodePtr parse() = 0;
};

std::shared_ptr<Parser> parser(std::shared_ptr<Lexer> lexer, 
							   std::shared_ptr<Error> error,
							   bool interactiveMode=false);

#endif //__parser_hh
