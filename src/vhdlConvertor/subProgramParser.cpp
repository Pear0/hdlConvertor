#include <hdlConvertor/vhdlConvertor/subProgramParser.h>
#include <hdlConvertor/vhdlConvertor/subProgramDeclarationParser.h>
#include <hdlConvertor/vhdlConvertor/literalParser.h>
#include <hdlConvertor/vhdlConvertor/statementParser.h>
#include <hdlConvertor/vhdlConvertor/exprParser.h>
#include <hdlConvertor/vhdlConvertor/interfaceParser.h>

namespace hdlConvertor {
namespace vhdl {

using namespace hdlConvertor::hdlObjects;
using vhdlParser = vhdl_antlr::vhdlParser;

HdlFunctionDef * SubProgramParser::visitSubprogram_body(
		vhdlParser::Subprogram_bodyContext* ctx) {
	// subprogram_body :
	// subprogram_specification IS
	// subprogram_declarative_part
	// BEGIN
	// subprogram_statement_part
	// END ( subprogram_kind )? ( designator )? SEMI
	// ;
	HdlFunctionDef * f = visitSubprogram_specification(
			ctx->subprogram_specification());

	auto vs = SubProgramDeclarationParser::visitSubprogram_declarative_part(
			ctx->subprogram_declarative_part());
	for (auto v : *vs) {
		f->locals.push_back(v);
	}
	delete vs;

	auto stmts = visitSubprogram_statement_part(
			ctx->subprogram_statement_part());
	for (auto s : *stmts) {
		f->body.push_back(s);
	}
	delete stmts;

	return f;
}

HdlFunctionDef * SubProgramParser::visitSubprogram_specification(
		vhdlParser::Subprogram_specificationContext* ctx) {
	// subprogram_specification
	// : procedure_specification
	// | function_specification
	// ;

	auto p = ctx->procedure_specification();
	if (p)
		return visitProcedure_specification(p);
	else
		return visitFunction_specification(ctx->function_specification());
}

HdlFunctionDef * SubProgramParser::visitProcedure_specification(
		vhdlParser::Procedure_specificationContext* ctx) {
	// procedure_specification
	// : PROCEDURE designator ( LPAREN formal_parameter_list RPAREN )?
	// ;
	auto designator = ctx->designator();
	iHdlExpr * returnT = NULL;
	bool isOperator = LiteralParser::isStrDesignator(designator);
	auto name = LiteralParser::visitDesignator(designator);

	auto fpl = ctx->formal_parameter_list();
	std::vector<HdlVariableDef*> * paramList = new std::vector<HdlVariableDef*>();
	if (fpl)
		paramList = visitFormal_parameter_list(fpl);

	return new HdlFunctionDef(name, isOperator, returnT, paramList);
}

HdlFunctionDef * SubProgramParser::visitFunction_specification(
		vhdlParser::Function_specificationContext* ctx) {
	// function_specification:
	//       ( PURE IMPURE )? FUNCTION designator
	//           subprogram_header
	//           ( ( PARAMETER )? LPAREN formal_parameter_list RPAREN )? RETURN type_mark
	// ;
	auto designator = ctx->designator();
	iHdlExpr * returnT = ExprParser::visitType_mark(ctx->type_mark());
	assert(returnT);

	bool isOperator = LiteralParser::isStrDesignator(designator);
	auto name = LiteralParser::visitDesignator(designator);

	auto fpl = ctx->formal_parameter_list();
	std::vector<HdlVariableDef*> * paramList = new std::vector<HdlVariableDef*>();
	if (fpl)
		paramList = visitFormal_parameter_list(fpl);

	return new HdlFunctionDef(name, isOperator, returnT, paramList);
}

std::vector<HdlVariableDef*> * SubProgramParser::visitFormal_parameter_list(
		vhdlParser::Formal_parameter_listContext* ctx) {
	// formal_parameter_list
	// : interface_list
	// ;
	return InterfaceParser::visitInterface_list(ctx->interface_list());
}

std::vector<iHdlStatement *> * SubProgramParser::visitSubprogram_statement_part(
		vhdlParser::Subprogram_statement_partContext* ctx) {
	// subprogram_statement_part
	// : ( sequential_statement )*
	// ;
	std::vector<iHdlStatement *> * statements = new std::vector<iHdlStatement*>();
	for (auto s : ctx->sequential_statement()) {
		statements->push_back(StatementParser::visitSequential_statement(s));
	}
	return statements;
}

}
}
