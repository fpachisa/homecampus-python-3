'''
Created on 30-Aug-2016

@author: Riyaz Ali
'''

'''
Name-Mapping Structure
----------------------
<Grade> = {                    0            1                2            3
        "sub-topic-url": [ <Filename>, <PracticeURL>, <WorksheetURL>, <VideoID>,
                               4            5           6
                           <Heading>, <Group ID>, <Self Index>]
    }

Object-format Mapping
---------------------
obj = {
    "url": [< 1 >, < 2 >],
    "videoID": < 3 >
    "heading": < 4 >,
    "LinkMap": < LinkMap corrs. to the Grade >,
    "GroupID": < 5 >,
    "selfAtPosition": < 6>
}

Link-Map Structure
------------------
LinkMap_<grade> = {
    "GroupID": ( "Group Title",
            [    -> List Containing Topic Name - URL mapped as Tuples
             (Topic Name, URL),
            ]
        ),
    .
    .
    .
}


'''

# LearnMappings for PRIMARY - 3
#------------------------------
Primary3 = {
        
        # Chapter - 1 WHOLE NUMBER
        "Multiplication-Tables-of-6-7-8-9": [
                "/WholeNumbers/Multiplication_Tables_Of_6_7_8_9.html", "", "", "",
                "Tips to Remember Multipication Tables", "P3WN", 1
            ],
        "Number-Notations-Place-Values-Up-to-10000": [
                "/WholeNumbers/Whole_Numbers_Upto_10000.html", "/Whole_Numbers_Number_Notation_Place_Values", "/Whole_Numbers_Number_Notation_Place_Values", "",
                "Number Notation and Place Values Up To 10000", "P3WN", 2
            ],
        "Writing-Numbers-from-Figures-to-Words-Up-to-10000": [
                "/WholeNumbers/Figures_To_Words_Upto_10000.html", "/Whole_Numbers_Figures_to_Words", "/Whole_Numbers_Figures_to_Words", "",
                "Writing Numbers from Figures to Words (Up To 10000)", "P3WN", 3
            ],
        "Writing-Numbers-from-Words-to-Figures-Up-to-10000": [
                "/WholeNumbers/Words_To_Figures_Upto_10000.html", "/Whole_Numbers_Words_to_Figures", "/Whole_Numbers_Words_to_Figures", "",
                "Writing Numbers from Words to Figures (Up To 10000)", "P3WN", 4
            ],
        "Number-Patterns": [
                "/WholeNumbers/Number_Patterns.html", "/Whole_Numbers_Patterns", "/Whole_Numbers_Patterns", "",
                "Number Patterns", "P3WN", 5
            ],
        "Comparing-Ordering": [
                "/WholeNumbers/Comparing_Ordering.html", "/Whole_Numbers_Comparing_Ordering", "/Whole_Numbers_Comparing_Ordering", "",
                "Comparing and Ordering Numbers", "P3WN", 6
            ],
        "Addition": [
                "/WholeNumbers/Addition_Of_Numbers_Within_10000.html", "/Whole_Numbers_Addition", "/Whole_Numbers_Addition", "",
                "Addition of Numbers Within 10000", "P3WN", 7
            ],
        "Subtraction": [
                "/WholeNumbers/Subtraction_Of_Numbers_Within_10000.html", "/Whole_Numbers_Subtraction", "/Whole_Numbers_Subtraction", "",
                "Subtraction of Numbers Within 10000", "P3WN", 8
            ],
        "Whole-Numbers-Multiplication": [
                "/WholeNumbers/Multiplication_Of_Numbers_Within_10000.html", "/Whole_Numbers_Multiplication", "/Whole_Numbers_Multiplication", "",
                "Multiplication of Numbers Within 10000", "P3WN", 9
            ],
        "Whole-Numbers-Division": [
                "/WholeNumbers/Division_Of_Numbers_Within_1000.html", "/Whole_Numbers_Division", "/Whole_Numbers_Division", "",
                "Division of Numbers Within 1000", "P3WN", 10
            ],        
        "2-Step-Word-Problems": [
                "/WholeNumbers/Whole_Numbers_Word_Problems.html", "/Whole_Numbers_Word_Problems", "/Whole_Numbers_Word_Problems", "",
                "2-Step Word Problems Involving the Four Operations (&plus;, &minus;, &times; and &divide;)", "P3WN", 11
            ],
        #----- END of CH - 1 -----#
        
        
    
  "Tables-and-Bar-Graphs": [
    "/Learn/Primary4/Data-Analysis/Tables-and-Bar-Graphs.html",
    "/Learn/P4DataAnalysisTablesBar",
    "/Learn/P4DataAnalysisTablesBar",
    "",
    "Tables and Bar Graphs",
    "P4DA",
    1
  ],
  "Line-Graphs": [
    "/Learn/Primary4/Data-Analysis/Line-Graphs.html",
    "/Learn/P4DataAnalysisLineGraphs",
    "/Learn/P4DataAnalysisLineGraphs",
    "",
    "Line Graphs",
    "P4DA",
    2
  ],
  "Perpendicular-and-Parallel-Lines": [
    "/Learn/Primary4/Geometry/Perpendicular-and-Parallel-Lines.html",
    "/Learn/P4GeometryParallelPerpendicular",
    "/Learn/P4GeometryParallelPerpendicular",
    "",
    "Perpendicular and Parallel Lines",
    "P4G",
    1
  ],
  "Understanding-Angles": [
    "/Learn/Primary4/Geometry/Understanding-Angles.html",
    "/Learn/P4GeometryUnderstandingAngles",
    "/Learn/P4GeometryUnderstandingAngles",
    "",
    "Understanding Angles",
    "P4G",
    2
  ],
  "What-is-an-angle-how-to-measure-it": [
    "/Learn/Primary4/Geometry/What-is-an-angle-how-to-measure-it.html",
    "/Learn/P4GeometryWhatisanAngle",
    "/Learn/P4GeometryWhatisanAngle",
    "",
    "What is an Angle & How to Measure It",
    "P4G",
    3
  ],
  "Drawing-Angles": [
    "/Learn/Primary4/Geometry/Drawing-Angles.html",
    "/Learn/P4GeometryDrawingAngles",
    "/Learn/P4GeometryDrawingAngles",
    "",
    "Drawing Angles",
    "P4Geometry",
    4
  ],
  "Angles-Turns-and-Directions": [
    "/Learn/Primary4/Geometry/Angles-Turns-and-Directions.html",
    "/Learn/P4GeometryAnglesTurnsDirections",
    "/Learn/P4GeometryAnglesTurnsDirections",
    "",
    "Angles, Turns and Directions",
    "P4Geometry",
    5
  ],
  "Quadrilaterals-Rectangles-and-Squares": [
    "/Learn/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares.html",
    "/Learn/P4GeometryQuadrilateral",
    "/Learn/P4GeometryQuadrilateral",
    "",
    "Quadrilaterals, Rectangles and Squares",
    "P4Geometry",
    6
  ],
  "Symmetric-Figures-Shapes-and-Patterns": [
    "/Learn/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns.html",
    "/Learn/P4GeometrySymmetry",
    "/Learn/P4GeometrySymmetry",
    "",
    "Symmetric Figures, Shapes and Patterns",
    "P4Geometry",
    7
  ],
  "Area-and-Perimeter-of-Rectangles-and-Squares": [
    "/Learn/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares.html",
    "/Learn/P4MeasurementRectangleSquare",
    "/Learn/P4MeasurementRectangleSquare",
    "",
    "Area and Perimeter of Rectangles and Squares",
    "P4Measurement",
    1
  ],
  "Time-Seconds-24-Hour-Clock-Duration": [
    "/Learn/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration.html",
    "/Learn/P4MeasurementTime",
    "/Learn/P4MeasurementTime",
    "",
    "Time, Seconds, 24-Hour Clock and Duration",
    "P4Measurement",
    2
  ],
  "Word-Problems-Whole-Numbers": [
    "/Learn/Primary4/Whole-Numbers/Word-Problems.html",
    "/Learn/P4WNWordProblems",
    "/Learn/P4WNWordProblems",
    "",
    "Whole Numbers – Word Problems",
    "P4WN",
    1
  ],
  "Factors-Multiples": [
    "/Learn/Primary4/Whole-Numbers/Factors-Multiples.html",
    "/Learn/P4WNFactorsMultiples",
    "/Learn/P4WNFactorsMultiples",
    "",
    "Factors and Multiples",
    "P4WN",
    2
  ],
  "Numbers-Up-to-100000": [
    "/Learn/Primary4/Whole-Numbers/Numbers-Up-to-100000.html",
    "/Learn/P4WNUpto100000",
    "/Learn/P4WNUpto100000",
    "",
    "Numbers Up to 100000",
    "P4WN",
    3
  ],
  "Multiplication-Division-by-1-and-2-Digit-Numbers": [
    "/Learn/Primary4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers.html",
    "/Learn/P4WNMultiplyDivide",
    "/Learn/P4WNMultiplyDivide",
    "",
    "Multiplication and Division by 1 and 2 Digit Numbers",
    "P4WN",
    4
  ],
  "Understanding-Tenths-Hundredths-Thousandths": [
    "/Learn/Primary4/Decimals/Understanding-Tenths-Hundredths-Thousandths.html",
    "/Learn/P4Decimal10s100s1000s",
    "/Learn/P4Decimal10s100s1000s",
    "",
    "Understanding Tenths, Hundredths and Thousandths",
    "P4Decimal",
    1
  ],
  "Decimals-Addition": [
    "/Learn/Primary4/Decimals/Decimals-Addition.html",
    "/Learn/P4DecimalAddition",
    "/Learn/P4DecimalAddition",
    "",
    "Decimal Addition",
    "P4Decimal",
    2
  ],
  "Decimals-Subtraction": [
    "/Learn/Primary4/Decimal/Decimals-Subtraction.html",
    "/Learn/P4DecimalSubtraction",
    "/Learn/P4DecimalSubtraction",
    "",
    "Decimal Subtraction",
    "P4Decimal",
    3
  ],
  "Decimals-Multiplication": [
    "/Learn/Primary4/Decimals/Decimals-Multiplication.html",
    "/Learn/P4DecimalMultiplication",
    "/Learn/P4DecimalMultiplication",
    "",
    "Decimal Multiplication",
    "P4Decimal",
    4
  ],
  "Decimals-Division": [
    "/Learn/Primary4/Decimals/Decimals-Division.html",
    "/Learn/P4DecimalDivision",
    "/Learn/P4DecimalDivision",
    "",
    "Decimal Division",
    "P4Decimal",
    5
  ],
  "Word-Problems-Decimals": [
    "/Learn/Primary4/Decimals/Word-Problems.html",
    "/Learn/P4DecimalWordProblems",
    "/Learn/P4DecimalWordProblems",
    "",
    "Word Problems – Decimals",
    "P4Decimal",
    6
  ],
  "Fractions-Word-Problems-Grade-4": [
    "/Learn/Primary4/Fractions/Fractions-Word-Problems-Grade-4.html",
    "/Learn/P4FractionsWordProblems",
    "/Learn/P4FractionsWordProblems",
    "",
    "Fractions – Word Problems (Grade 4)",
    "P4Fractions",
    1
  ],
  
  "Fraction-of-a-Set": [
    "/Learn/Primary-Grade-4/Fractions/Fraction-of-a-Set.html",
    "/Learn/P4FractionsOfSet",
    "/Learn/P4FractionsOfSet",
    "",
    "Fraction of a Set",
    "P4Fractions",
    2
  ],
  "Types-of-Fractions": [
    "/Learn/Primary-Grade-4/Types-of-Fractions.html",
    "/Learn/P5FRTypesFractions",
    "/Learn/P5FRTypesFractions",
    "",
    "Types of Fractions",
    "P4Fractions",
    3
  ],
  "Simplifying-Fractions-GCF": [
    "/Learn/Primary-Grade-4/Fractions/Simplifying-Fractions-GCF.html",
    "/Learn/P5FRSimplifyingFractions",
    "/Learn/P5FRSimplifyingFractions",
    "",
    "Simplifying Fractions using GCF",
    "P4Fractions",
    4
  ],
  "Mixed-Numbers-Improper-Fractions": [
    "/Learn/Primary-Grade-4/Fractions/Mixed-Numbers-Improper-Fractions.html",
    "/Learn/P5FRImproperMixedFractions",
    "/Learn/P5FRImproperMixedFractions",
    "",
    "Mixed Numbers and Improper Fractions",
    "P4Fractions",
    5
  ],
  "Addition-Proper-Fractions": [
    "/Learn/Primary-Grade-4/Fractions/Addition-Proper-Fractions.html",
    "/Learn/P5FRAddProperFractions",
    "/Learn/P5FRAddProperFractions",
    "",
    "Addition of Proper Fractions",
    "P4Fractions",
    6
  ],
  "Subtraction-Proper-Fractions": [
    "/Learn/Primary-Grade-4/Fractions/Subtraction-Proper-Fractions.html",
    "/Learn/P5FRSubProperFractions",
    "/Learn/P5FRSubProperFractions",
    "",
    "Subtraction of Proper Fractions",
    "P4Fractions",
    7
  ],


#primary5
 
  "Figures-to-Words": [
    "/Learn/Primary5/WholeNumbers/Figures-to-Words.html",
    "/Learn/P5WNFiguresToWords",
    "/Learn/P5WNFiguresToWords",
    "",
    "Figures to Words",
    "P5WholeNumbers",
    1
  ],
  "Words-to-Figures": [
    "/Learn/Primary5/WholeNumbers/Words-to-Figures.html",
    "/Learn/P5WNWordsToFigures",
    "/Learn/P5WNWordsToFigures",
    "",
    "Words to Figures",
    "P5WholeNumbers",
    2
  ],
  "Place-Values": [
    "/Learn/Primary5/WholeNumbers/Place-Values.html",
    "/Learn/P5WNPlaceValue",
    "/Learn/P5WNPlaceValue",
    "",
    "Place Values",
    "P5WholeNumbers",
    3
  ],
  "Comparison-Ordering-Pattern": [
    "/Learn/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html",
    "/Learn/P5WNComparisonOrdering",
    "/Learn/P5WNComparisonOrdering",
    "",
    "Comparison, Ordering & Pattern",
    "P5WholeNumbers",
    4
  ],
  "Approximation-Estimation-Part-1": [
    "/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-1.html",
    "/Learn/P5WNApproximationEstimation1",
    "/Learn/P5WNApproximationEstimation1",
    "",
    "Approximation & Estimation Part 1",
    "P5WholeNumbers",
    5
  ],
  "Approximation-Estimation-Part-2": [
    "/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-2.html",
    "/Learn/P5WNApproximationEstimation2",
    "/Learn/P5WNApproximationEstimation2",
    "",
    "Approximation & Estimation Part 2",
    "P5WholeNumbers",
    6
  ],
  "Multiply-by-10-100-1000": [
    "/Learn/Primary5/WholeNumbers/Multiply-by-10-100-1000.html",
    "/Learn/P5WNMultiply",
    "/Learn/P5WNMultiply",
    "",
    "Multiply by 10, 100, 1000",
    "P5WholeNumbers",
    7
  ],
  "Divide-by-10-100-1000": [
    "/Learn/Primary5/WholeNumbers/Divide-by-10-100-1000.html",
    "/Learn/P5WNDivide",
    "/Learn/P5WNDivide",
    "",
    "Divide by 10, 100, 1000",
    "P5WholeNumbers",
    8
  ],
  "Order-of-Operations": [
    "/Learn/Primary5/WholeNumbers/Order-of-Operations.html",
    "/Learn/P5WNOperations",
    "/Learn/P5WNOperations",
    "",
    "Order of Operations",
    "P5WholeNumbers",
    9
  ],
  "What-Is-a-Fraction": [
    "/Learn/Primary5/Fractions/What-Is-a-Fraction.html",
    "/Learn/P5FRWhatIsFractions",
    "/Learn/P5FRWhatIsFractions",
    "",
    "What Is a Fraction?",
    "P5Fractions",
    1
  ],
  "Types-of-Fractions": [
    "/Learn/Primary5/Fractions/Types-of-Fractions.html",
    "/Learn/P5FRTypesFractions",
    "/Learn/P5FRTypesFractions",
    "",
    "Types of Fractions",
    "P5Fractions",
    2
  ],
  "Improper-Mixed-Fractions": [
    "/Learn/Primary5/Fractions/Improper-Mixed-Fractions.html",
    "/Learn/P5FRImproperMixedFractions",
    "/Learn/P5FRImproperMixedFractions",
    "",
    "Improper & Mixed Fractions",
    "P5Fractions",
    3
  ],
  "Simplifying-Fractions-GCF": [
    "/Learn/Primary5/Fractions/Simplifying-Fractions-GCF.html",
    "/Learn/P5FRSimplifyingFractions",
    "/Learn/P5FRSimplifyingFractions",
    "",
    "Simplifying Fractions using GCF",
    "P5Fractions",
    4
  ],
  "Addition-Proper-Fractions": [
    "/Learn/Primary5/Fractions/Addition-Proper-Fractions.html",
    "/Learn/P5FRAddProperFractions",
    "/Learn/P5FRAddProperFractions",
    "",
    "Addition of Proper Fractions",
    "P5Fractions",
    5
  ],
  "Subtraction-Proper-Fractions": [
    "/Learn/Primary5/Fractions/Subtraction-Proper-Fractions.html",
    "/Learn/P5FRSubProperFractions",
    "/Learn/P5FRSubProperFractions",
    "",
    "Subtraction of Proper Fractions",
    "P5Fractions",
    6
  ],
  "Addition-Mixed-Fractions": [
    "/Learn/Primary5/Fractions/Addition-Mixed-Fractions.html",
    "/Learn/P5FRAddMixedFractions",
    "/Learn/P5FRAddMixedFractions",
    "",
    "Addition of Mixed Fractions",
    "P5Fractions",
    7
  ],
  "Subtraction-Mixed-Fractions": [
    "/Learn/Primary5/Fractions/Subtraction-Mixed-Fractions.html",
    "/Learn/P5FRSubMixedFractions",
    "/Learn/P5FRSubMixedFractions",
    "",
    "Subtraction of Mixed Fractions",
    "P5Fractions",
    8
  ],
  "Multiplication-Fractions": [
    "/Learn/Primary5/Fractions/Multiplication-Fractions.html",
    "/Learn/P5FRMultFractions",
    "/Learn/P5FRMultFractions",
    "",
    "Multiplication of Fractions",
    "P5Fractions",
    9
  ],
  "Multiplication-Mixed-Fractions": [
    "/Learn/Primary5/Fractions/Multiplication-Mixed-Fractions.html",
    "/Learn/P5FRMultMixedFractions",
    "/Learn/P5FRMultMixedFractions",
    "",
    "Multiplication of Mixed Fractions",
    "P5Fractions",
    10
  ],
  "Division-Proper-Fraction": [
    "/Learn/Primary5/Fractions/Division-Proper-Fraction.html",
    "/Learn/P5FRDivisionFractions",
    "/Learn/P5FRDivisionFractions",
    "",
    "Division of Proper Fractions",
    "P5Fractions",
    11
  ],
  "Fraction-as-Division": [
    "/Learn/Primary5/Fractions/Fraction-as-Division.html",
    "/Learn/P5FRFractionDivision",
    "/Learn/P5FRFractionDivision",
    "",
    "Fraction as Division",
    "P5Fractions",
    12
  ],
  "Fractions-Decimals": [
    "/Learn/Primary5/Fractions/Fractions-Decimals.html",
    "/Learn/P5FRFractionDecimal",
    "/Learn/P5FRFractionDecimal",
    "",
    "Fractions and Decimals",
    "P5Fractions",
    13
  ],
  "Multiply-Decimal-by-10-100-1000": [
    "/Learn/Primary5/Decimal/Multiply-by-10-100-1000.html",
    "/Learn/P5DCMultiply",
    "/Learn/P5DCMultiply",
    "",
    "Multiply Decimals by 10, 100, 1000",
    "P5Decimal",
    1
  ],
  "Divide-Decimal-by-10-100-1000": [
    "/Learn/Primary5/Decimal/Divide-by-10-100-1000.html",
    "/Learn/P5DCDivide",
    "/Learn/P5DCDivide",
    "",
    "Divide Decimals by 10, 100, 1000",
    "P5Decimal",
    2
  ],
  "Rounding-Off-Decimal-Numbers": [
    "/Learn/Primary5/Decimal/Rounding-Off-Decimal-Numbers.html",
    "/Learn/P5DCRounding",
    "/Learn/P5DCRounding",
    "",
    "Rounding Off Decimal Numbers",
    "P5Decimal",
    3
  ],
  "Estimation-in-Decimal-Calculations": [
    "/Learn/Primary5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers.html",
    "/Learn/P5DCEstimation",
    "/Learn/P5DCEstimation",
    "",
    "Estimation in Decimal Calculations",
    "P5Decimal",
    4
  ],
  "Percentage-Introduction": [
    "/Learn/Primary5/Percentage/Introduction.html",
    "/Learn/P5PRIntroduction",
    "/Learn/P5PRIntroduction",
    "",
    "Introduction to Percentage",
    "P5Percentage",
    1
  ],
  "Percentage-and-Fractions": [
    "/Learn/Primary5/Percentage/Percentage-and-Fractions.html",
    "/Learn/P5PRFractions",
    "/Learn/P5PRFractions",
    "",
    "Percentage and Fractions",
    "P5Percentage",
    2
  ],
  "Percentage-and-Decimals": [
    "/Learn/Primary5/Percentage/Percentage-and-Decimals.html",
    "/Learn/P5PRDecimals",
    "/Learn/P5PRDecimals",
    "",
    "Percentage and Decimals",
    "P5Percentage",
    3
  ],
  "Ratio-Introduction": [
    "/Learn/Primary5/Ratio/Introduction.html",
    "/Learn/P5RTIntroduction",
    "/Learn/P5RTIntroduction",
    "",
    "Introduction to Ratio",
    "P5Ratio",
    1
  ],
  "Ratio-Equivalent": [
    "/Learn/Primary5/Ratio/Equivalent.html",
    "/Learn/P5RTEquivalent",
    "/Learn/P5RTEquivalent",
    "",
    "Equivalent Ratios",
    "P5Ratio",
    2
],

#primary 6
  "Dividing-Proper-Fraction-by-Proper-Fraction": [
    "/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction",
    "/Learn/P6ProperFractionProperFraction",
    "/Learn/P6ProperFractionProperFraction",
    "",
    "Dividing Proper Fraction by Proper Fraction",
    "P6Fractions",
    1
  ],
  "What-is-Algebra-and-Algebraic-Expressions": [
    "/Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions",
    "/Learn/P6AlgebraWhatIsAlgebra",
    "/Learn/P6AlgebraWhatIsAlgebra",
    "",
    "What is Algebra and Algebraic Expressions",
    "P6Algebra",
    1
  ],
  "Simplifying-and-Evaluating-Algebraic-Expressions": [
    "/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions",
    "/Learn/P6AlgebraSimplifying",
    "/Learn/P6AlgebraSimplifying",
    "",
    "Simplifying and Evaluating Algebraic Expressions",
    "P6Algebra",
    2
  ],
  "Finding-Whole-Given-Part-and-Percentage": [
    "/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage",
    "/Learn/P6PRFindWhole",
    "/Learn/P6PRFindWhole",
    "",
    "Finding Whole Given Part and Percentage",
    "P6Percentage",
    1
  ],
  "Finding-Percentage-Increase-Decrease": [
    "/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease",
    "/Learn/P6PRIncDec",
    "/Learn/P6PRIncDec",
    "",
    "Finding Percentage Increase Decrease",
    "P6Percentage",
    2
  ],
  "Advanced-Word-Problems": [
    "/Learn/Primary6/Percentage/Advanced-Word-Problems",
    "/Learn/P6PercentageWordProblems",
    "/Learn/P6PercentageWordProblems",
    "",
    "Advanced Word Problems",
    "P6Percentage",
    3
  ],
  "Distance-Time-Speed": [
    "/Learn/Primary6/Speed/Distance-Time-Speed",
    "/Learn/P6SpeedDistanceTime",
    "/Learn/P6SpeedDistanceTime",
    "",
    "Distance Time Speed",
    "P6Speed",
    1
  ],
  "Average-Speed": [
    "/Learn/Primary6/Speed/Average-Speed",
    "/Learn/P6SpeedAverage",
    "/Learn/P6SpeedAverage",
    "",
    "Average Speed",
    "P6Speed",
    2
  ],
  "Advanced-Word-Problems-Speed": [
    "/Learn/Primary6/Speed/Advanced-Word-Problems",
    "/Learn/P6SpeedAdvancedWordProblems",
    "/Learn/P6SpeedAdvancedWordProblems",
    "",
    "Advanced Word Problems",
    "P6Speed",
    3
  ],
  "Pie-Chart": [
    "/Learn/Primary6/Data-Analysis/Pie-Chart",
    "/Learn/P6DataAnalysisPieChart",
    "/Learn/P6DataAnalysisPieChart",
    "",
    "Pie Chart",
    "P6DataAnalysis",
    1
  ],
  "Pie-Chart-Word-Problems": [
    "/Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems",
    "/Learn/P6DataAnalysisPieChartWordProblems",
    "/Learn/P6DataAnalysisPieChartWordProblems",
    "",
    "Pie Chart Word Problems",
    "P6DataAnalysis",
    2
  ],
  "Word-Problems-Ratio": [
    "/Learn/Primary6/Ratio/Word-Problems",
    "/Learn/P6RatioWordProblems",
    "/Learn/P6RatioWordProblems",
    "",
    "Word Problems",
    "P6Ratio",
    1
  ],
  "Ratio-and-Fraction": [
    "/Learn/Primary6/Ratio/Ratio-and-Fraction",
    "/Learn/P6RatioFraction",
    "/Learn/P6RatioFraction",
    "",
    "Ratio and Fraction",
    "P6Ratio",
    2
  ],
  "Equivalent-Fraction-and-Ratio": [
    "/Learn/Primary6/Ratio/Equivalent-Fraction-and-Ratio",
    "/Learn/P6RatioEquivalentFraction",
    "/Learn/P6RatioEquivalentFraction",
    "",
    "Equivalent Fraction and Ratio",
    "P6Ratio",
    3
  ],
  "Volume-Cube-Cuboid-Advanced-Word-Problems": [
    "/Learn/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems",
    "/Learn/P6MeasurementWordProblems",
    "/Learn/P6MeasurementWordProblems",
    "",
    "Volume Cube Cuboid Advanced Word Problems",
    "P6Measurement",
    1
  ],
  "Radius-and-Diameter-of-Circle": [
    "/Learn/Primary6/Measurement/Radius-and-Diameter-of-Circle",
    "/Learn/P6MeasurementRadiusDiameter",
    "/Learn/P6MeasurementRadiusDiameter",
    "",
    "Radius and Diameter of Circle",
    "P6Measurement",
    2
  ],
  "Circumference-of-Circle": [
    "/Learn/Primary6/Measurement/Circumference-of-Circle",
    "/Learn/P6MeasurementCircleCircumference",
    "/Learn/P6MeasurementCircleCircumference",
    "",
    "Circumference of Circle",
    "P6Measurement",
    3
  ],
  "Area-of-Circle": [
    "/Learn/Primary6/Measurement/Area-of-Circle",
    "/Learn/P6MeasurementCircleArea",
    "/Learn/P6MeasurementCircleArea",
    "",
    "Area of Circle",
    "P6Measurement",
    4
  ],
  "Area-and-Perimeter-of-Composite-Figures": [
    "/Learn/Primary6/Area-and-Perimeter-of-Composite-Figures",
    "/Learn/P6MeasurementComposite",
    "/Learn/P6MeasurementComposite",
    "",
    "Area and Perimeter of Composite Figures",
    "P6Measurement",
    5
  ],
  "Finding-Unknown-Angles-Advanced-Problems": [
    "/Learn/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems",
    "/Learn/P6GeometryAdvancedProblems",
    "/Learn/P6GeometryAdvancedProblems",
    "",
    "Finding Unknown Angles Advanced Problems",
    "P6Geometry",
    1
  ],
  "Tips-To-Remember-Multiplication-Times-Table-Of-2-To-12": [
    "/Learn/Primary2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12",
    "/Learn/P2TimesTable",
    "/Learn/P2TimesTable",
    "",
    "Tips To Remember (Multiplication) Times Table Of 2 To 12",
    "P2WholeNumbers",
    1
  ]



}

# End of LearnMappings for PRIMARY - 3
#------------------------------

# Link Mapping for Sidebar PRIMARY - 3
#---------------------------------
LinkMap_P3 = [
        ( "P3WN", "Whole Numbers",
          [
           ("Multiplication Table of 6, 7, 8, 9", "/Learn/Primary-Grade-3/Whole-Numbers/Multiplication-Tables-of-6-7-8-9"),
           ("Numbers up to 10 000", "/Learn/Primary-Grade-3/Whole-Numbers/Number-Notations-Place-Values-Up-to-10000"), ("Figures to Words up to 10 000", "/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Figures-to-Words-Up-to-10000"),
           ("Words to Figures up to 10 000", "/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000"), ("Number Patterns", "/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000"),
           ("Comparing and Ordering", "/Learn/Primary-Grade-3/Whole-Numbers/Comparing-Ordering"), ("Addition", "/Learn/Primary-Grade-3/Whole-Numbers/Addition"),
           ("Subtraction", "/Learn/Primary-Grade-3/Whole-Numbers/Subtraction"), ("Multiplication", "/Learn/Primary-Grade-3/Whole-Numbers-Multiplication"),
           ("Division", "/Learn/Primary-Grade-3/Whole-Numbers-Division"), ("2 - Step Word Problems", "/Learn/Primary-Grade-3/Whole-Numbers/2-Step-Word-Problems")
          ]
        ),
        ( "P3MO", "Money",
          [
           ("Addition", "/Learn/Primary-Grade-3/Addition-of-Money"), ("Subtraction", "/Learn/Primary-Grade-3/Subtraction-of-Money"),
           ("Word Problems", "/Learn/Primary-Grade-3/Money-Word-Problems")
          ]
        ),
        ( "P3TI", "Time",
          [
           ("Telling Time", "/Learn/Primary-Grade-3/Telling-Time"), ("Hours and Minutes", "/Learn/Primary-Grade-3/Time-Conversion-Hours-Minutes"),
           ("Addition", "/Learn/Primary-Grade-3/Time-Subtraction"), ("Subtraction", "/Learn/Primary-Grade-3/Time-Subtraction"),
           ("Duration, Start and Finish Times", "/Learn/Primary-Grade-3/Time-Subtraction"), ("Word Problems", "/Learn/Primary-Grade-3/Time-Subtraction")
          ]
          )
    ]
# End of Link Mapping for Sidebar PRIMARY - 3
#---------------------------------

class Grade3Mapper:
    @classmethod
    def getMapping(cls, subTopic, topic=""):
        try:
            data = Primary3[subTopic]
        except KeyError:
            raise

        group_id = data[5]

        # Extract the group entry (ID, Title, List)
        relevant_link_map = next(
            (group for group in LinkMap_P3 if group[0] == group_id), None
        )

        group_title = relevant_link_map[1].replace(" ", "") if relevant_link_map else "Misc"

        obj = {
            'url': [data[1], data[2]],
            'videoID': data[3],
            'heading': data[4],
            'LinkMap': relevant_link_map,  # Only relevant group
            'GroupID': group_id,
            'selfAtPosition': data[6],
            'GroupTitle': group_title  # added group title for pathing
        }

        return data[0], obj


        
    
    