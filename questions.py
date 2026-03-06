questions = []

# =========================
# PHYSICS – 50 UNIQUE
# =========================

physics_data = [
("Dimensional formula of force?", ["MLT^-2", "ML^2T^-1", "M^2LT^-2", "ML^-1T^-2"], "MLT^-2"),
("Escape velocity of Earth?", ["11.2 km/s", "9.8 km/s", "7.9 km/s", "15 km/s"], "11.2 km/s"),
("SI unit of electric field?", ["N/C", "Volt", "Ohm", "Tesla"], "N/C"),
("Unit of magnetic flux?", ["Weber", "Tesla", "Henry", "Farad"], "Weber"),
("Work done in circular motion?", ["Zero", "Maximum", "Negative", "Infinite"], "Zero"),
("Ohm’s Law?", ["V=IR", "P=VI", "F=ma", "E=mc^2"], "V=IR"),
("Energy of photon?", ["E=hf", "mc^2", "mgh", "1/2mv^2"], "E=hf"),
("Unit of power?", ["Watt", "Joule", "Pascal", "Newton"], "Watt"),
("Momentum formula?", ["mv", "ma", "mgh", "1/2mv^2"], "mv"),
("Impulse equals?", ["Change in momentum", "Force", "Energy", "Velocity"], "Change in momentum"),
("Unit of frequency?", ["Hertz", "Second", "Meter", "Newton"], "Hertz"),
("Capacitance unit?", ["Farad", "Henry", "Ohm", "Tesla"], "Farad"),
("Inductor unit?", ["Henry", "Farad", "Ohm", "Watt"], "Henry"),
("Centripetal force formula?", ["mv^2/r", "mgh", "ma", "mv"], "mv^2/r"),
("Pressure unit?", ["Pascal", "Newton", "Joule", "Watt"], "Pascal"),
("Gravitational force formula?", ["GMm/r^2", "F=ma", "mgh", "mv^2/r"], "GMm/r^2"),
("Hooke’s law?", ["F=-kx", "F=ma", "V=IR", "E=hf"], "F=-kx"),
("Snell’s law?", ["n1sinθ1=n2sinθ2", "F=ma", "V=IR", "E=mc^2"], "n1sinθ1=n2sinθ2"),
("Angular momentum?", ["r×p", "mv", "ma", "mgh"], "r×p"),
("Unit of charge?", ["Coulomb", "Ampere", "Volt", "Ohm"], "Coulomb"),
("Wave speed formula?", ["v=fλ", "v=u+at", "V=IR", "E=hf"], "v=fλ"),
("Kinetic energy?", ["1/2mv^2", "mv", "ma", "mgh"], "1/2mv^2"),
("Potential energy?", ["mgh", "mv", "ma", "hf"], "mgh"),
("Acceleration unit?", ["m/s^2", "m/s", "kg", "N"], "m/s^2"),
("Momentum unit?", ["kg m/s", "Newton", "Joule", "Pascal"], "kg m/s"),
("Power formula?", ["P=VI", "V=IR", "E=mc^2", "F=ma"], "P=VI"),
("Current formula?", ["I=Q/t", "V=IR", "P=VI", "F=ma"], "I=Q/t"),
("Frequency formula?", ["f=1/T", "T=1/f", "v=fλ", "P=VI"], "f=1/T"),
("Unit of temperature?", ["Kelvin", "Celsius", "Watt", "Tesla"], "Kelvin"),
("Photoelectric effect shows light is?", ["Particle", "Wave", "Sound", "Mechanical"], "Particle"),
("Gauss law relates flux to?", ["Charge enclosed", "Current", "Voltage", "Resistance"], "Charge enclosed"),
("Mirror formula?", ["1/f=1/v+1/u", "V=IR", "F=ma", "E=mc^2"], "1/f=1/v+1/u"),
("Lens formula?", ["1/f=1/v-1/u", "V=IR", "F=ma", "E=hf"], "1/f=1/v-1/u"),
("Unit of magnetic field?", ["Tesla", "Weber", "Henry", "Ohm"], "Tesla"),
("Unit of resistivity?", ["Ohm m", "Ohm", "Volt", "Tesla"], "Ohm m"),
("Acceleration due to gravity?", ["9.8 m/s^2", "10 m/s", "8.9", "11"], "9.8 m/s^2"),
("Torque formula?", ["τ=rF", "F=ma", "mv", "mgh"], "τ=rF"),
("Energy unit?", ["Joule", "Watt", "Newton", "Tesla"], "Joule"),
("Unit of wavelength?", ["Meter", "Second", "Hertz", "Newton"], "Meter"),
("Bohr model applicable to?", ["Hydrogen atom", "All atoms", "Molecules", "Neutron"], "Hydrogen atom"),
("EMF unit?", ["Volt", "Ampere", "Ohm", "Farad"], "Volt"),
("Drift velocity depends on?", ["Electric field", "Mass only", "Charge only", "Temperature only"], "Electric field"),
("Unit of angular velocity?", ["rad/s", "m/s", "s", "kg"], "rad/s"),
("Heat unit?", ["Joule", "Watt", "Pascal", "Tesla"], "Joule"),
("Unit of force?", ["Newton", "Joule", "Pascal", "Watt"], "Newton"),
("Work formula?", ["W=Fd", "F=ma", "V=IR", "E=hf"], "W=Fd"),
("Pressure formula?", ["P=F/A", "F=ma", "V=IR", "P=VI"], "P=F/A"),
("Gravitational potential energy?", ["-GMm/r", "mgh", "mv", "ma"], "-GMm/r"),
("Unit of capacitance?", ["Farad", "Henry", "Ohm", "Tesla"], "Farad")
]

# =========================
# CHEMISTRY – 50 UNIQUE
# =========================

chemistry_data = [
("pH of 0.01 M HCl solution is?", ["2", "1", "3", "4"], "2"),
("Hybridization of BF3 is?", ["sp2", "sp3", "sp", "dsp2"], "sp2"),
("Strongest intermolecular force in water?", ["Hydrogen bonding", "Van der Waals", "Dipole force", "Ionic"], "Hydrogen bonding"),
("Oxidation number of Mn in KMnO4?", ["+7", "+5", "+2", "+4"], "+7"),
("Unit of rate of reaction?", ["mol L-1 s-1", "mol", "L", "atm"], "mol L-1 s-1"),
("Avogadro number value?", ["6.022×10^23", "3×10^8", "9.8", "1.6×10^-19"], "6.022×10^23"),
("Gas with highest diffusion rate?", ["H2", "O2", "N2", "CO2"], "H2"),
("Bond order of O2?", ["2", "1", "3", "0"], "2"),
("Shape of NH3 molecule?", ["Trigonal pyramidal", "Linear", "Tetrahedral", "Octahedral"], "Trigonal pyramidal"),
("Strong electrolyte example?", ["NaCl", "Sugar", "Urea", "Glucose"], "NaCl"),
("Catalyst changes?", ["Activation energy", "ΔH", "Product", "Equilibrium constant"], "Activation energy"),
("Entropy increases in?", ["Melting of ice", "Freezing", "Condensation", "Deposition"], "Melting of ice"),
("Enthalpy unit?", ["kJ/mol", "Watt", "Pascal", "Volt"], "kJ/mol"),
("IUPAC name of CH3COOH?", ["Ethanoic acid", "Methanoic acid", "Propanol", "Ethanol"], "Ethanoic acid"),
("Alkene general formula?", ["CnH2n", "CnH2n+2", "CnH2n-2", "CnHn"], "CnH2n"),
("Most electronegative element?", ["Fluorine", "Oxygen", "Chlorine", "Nitrogen"], "Fluorine"),
("Acid according to Bronsted theory?", ["Proton donor", "Electron donor", "Proton acceptor", "Salt"], "Proton donor"),
("Reducing agent?", ["Gives electrons", "Takes electrons", "Neutral", "Catalyst"], "Gives electrons"),
("Ideal solution obeys?", ["Raoult’s law", "Boyle’s law", "Charles law", "Graham law"], "Raoult’s law"),
("Molarity formula?", ["moles/volume(L)", "mass/volume", "moles/mass", "mass/moles"], "moles/volume(L)"),
("SI unit of pressure?", ["Pascal", "atm", "bar", "mmHg"], "Pascal"),
("Hybridization of C in C2H4?", ["sp2", "sp3", "sp", "dsp2"], "sp2"),
("Strong base example?", ["NaOH", "NH4OH", "CH3COOH", "H2O"], "NaOH"),
("Coordination number in NaCl?", ["6", "4", "8", "2"], "6"),
("Ozone is?", ["Allotrope of oxygen", "Compound", "Radical", "Ion"], "Allotrope of oxygen"),
("Half-life depends on?", ["Rate constant", "Initial concentration", "Temperature only", "Pressure"], "Rate constant"),
("Colloidal particles size range?", ["1-1000 nm", ">1000 nm", "<1 nm", "1 mm"], "1-1000 nm"),
("Orbital shape of p-orbital?", ["Dumbbell", "Spherical", "Circular", "Linear"], "Dumbbell"),
("Primary alcohol example?", ["CH3CH2OH", "CH3CHOHCH3", "CH3COOH", "CH3OCH3"], "CH3CH2OH"),
("Aldehyde functional group?", ["-CHO", "-COOH", "-OH", "-NH2"], "-CHO"),
("Carboxylic acid group?", ["-COOH", "-OH", "-CHO", "-NH2"], "-COOH"),
("Phenol is?", ["Weak acid", "Strong acid", "Neutral", "Salt"], "Weak acid"),
("Isomerism in C4H10?", ["2", "1", "3", "4"], "2"),
("Atomic radius decreases across period due to?", ["Nuclear charge", "Mass", "Neutrons", "Orbitals"], "Nuclear charge"),
("Electrochemical series based on?", ["Reduction potential", "Mass", "Size", "Color"], "Reduction potential"),
("Faraday constant approx?", ["96500 C/mol", "1000", "9.8", "6.022"], "96500 C/mol"),
("Le Chatelier principle predicts?", ["Shift in equilibrium", "Rate", "Pressure", "Volume"], "Shift in equilibrium"),
("d-block elements called?", ["Transition metals", "Noble gases", "Alkali", "Halogens"], "Transition metals"),
("Greenhouse gas?", ["CO2", "O2", "N2", "H2"], "CO2"),
("Water hardness due to?", ["Ca2+, Mg2+", "Na+", "K+", "Cl-"], "Ca2+, Mg2+"),
("Buffer solution resists change in?", ["pH", "Temperature", "Pressure", "Volume"], "pH"),
("SN1 reaction intermediate?", ["Carbocation", "Radical", "Anion", "Base"], "Carbocation"),
("Most stable carbocation?", ["Tertiary", "Primary", "Methyl", "Secondary"], "Tertiary"),
("Alkyne general formula?", ["CnH2n-2", "CnH2n", "CnH2n+2", "CnHn"], "CnH2n-2"),
("Metallic bonding involves?", ["Delocalized electrons", "Protons", "Neutrons", "Covalent pair"], "Delocalized electrons"),
("Oxidation involves?", ["Increase in oxidation number", "Decrease", "Neutral", "Constant"], "Increase in oxidation number"),
("Boiling point increases with?", ["Intermolecular force", "Mass only", "Color", "Density"], "Intermolecular force"),
("Pauli exclusion principle states?", ["No two electrons same quantum numbers", "Energy same", "Mass same", "Charge same"], "No two electrons same quantum numbers"),
("Valency of carbon?", ["4", "2", "1", "3"], "4")
]


# =========================
# MATHEMATICS – 50 UNIQUE
# =========================

math_data = [
("Derivative of sin x?", ["cos x", "-cos x", "sin x", "-sin x"], "cos x"),
("Integral of e^x dx?", ["e^x", "xe^x", "ln x", "1/x"], "e^x"),
("Value of sin 90°?", ["1", "0", "-1", "1/2"], "1"),
("Determinant of identity matrix?", ["1", "0", "n", "-1"], "1"),
("If discriminant >0 roots are?", ["Real & distinct", "Equal", "Imaginary", "Zero"], "Real & distinct"),
("Slope formula?", ["(y2-y1)/(x2-x1)", "x+y", "xy", "y/x"], "(y2-y1)/(x2-x1)"),
("Probability range?", ["0 to 1", "0 to 10", "-1 to 1", "1 to 10"], "0 to 1"),
("Limit of sinx/x?", ["1", "0", "∞", "-1"], "1"),
("Equation of circle?", ["x2+y2=r2", "x+y=r", "xy=r", "x2-y2=r2"], "x2+y2=r2"),
("cos2θ identity?", ["1-sin2θ", "sin2θ", "1+sin2θ", "tanθ"], "1-sin2θ"),
("Derivative of ln x?", ["1/x", "x", "ln x", "e^x"], "1/x"),
("Mean of data?", ["Sum/n", "n/sum", "sum×n", "n²"], "Sum/n"),
("Matrix multiplication condition?", ["Columns A = Rows B", "Rows equal", "Square only", "None"], "Columns A = Rows B"),
("Integration of 1 dx?", ["x", "1", "0", "ln x"], "x"),
("sin(A+B)?", ["sinAcosB+cosAsinB", "sinA+sinB", "cosA+cosB", "tanA+tanB"], "sinAcosB+cosAsinB"),
("Area under curve gives?", ["Integration", "Differentiation", "Limit", "Matrix"], "Integration"),
("Standard deviation measures?", ["Dispersion", "Mean", "Median", "Mode"], "Dispersion"),
("tanθ = ?", ["sinθ/cosθ", "cosθ/sinθ", "1/sinθ", "1/cosθ"], "sinθ/cosθ"),
("If A∩B=∅ sets are?", ["Disjoint", "Equal", "Universal", "Subset"], "Disjoint"),
("Permutation formula?", ["n!", "n²", "n", "n/2"], "n!"),
("Combination formula?", ["nCr", "nPr", "n!", "n²"], "nCr"),
("Determinant of 2x2 matrix?", ["ad-bc", "a+b", "ab", "a-b"], "ad-bc"),
("Derivative of x3?", ["3x2", "x3", "2x", "x2"], "3x2"),
("Integral of cos x?", ["sin x", "-sin x", "cos x", "-cos x"], "sin x"),
("Distance formula?", ["√[(x2-x1)2+(y2-y1)2]", "x+y", "xy", "y/x"], "√[(x2-x1)2+(y2-y1)2]"),
("Equation of straight line?", ["y=mx+c", "x+y=r", "xy=c", "x2+y2=r2"], "y=mx+c"),
("Derivative of tan x?", ["sec2x", "cosec2x", "sinx", "cosx"], "sec2x"),
("Value of log10 100?", ["2", "1", "10", "0"], "2"),
("Binomial theorem applies to?", ["(a+b)n", "a+b", "a-b", "ab"], "(a+b)n"),
("Vector magnitude formula?", ["√(x2+y2+z2)", "x+y+z", "xyz", "x-y"], "√(x2+y2+z2)"),
("Probability of impossible event?", ["0", "1", "1/2", "-1"], "0"),
("Derivative of constant?", ["0", "1", "x", "∞"], "0"),
("If sinθ=1 then θ=?", ["90°", "0°", "45°", "60°"], "90°"),
("Matrix transpose swaps?", ["Rows & columns", "Values", "Signs", "Diagonal"], "Rows & columns"),
("Mean of first n natural numbers?", ["(n+1)/2", "n/2", "n", "2n"], "(n+1)/2"),
("If cosθ=0 then θ=?", ["90°", "0°", "45°", "30°"], "90°"),
("Derivative of e^x?", ["e^x", "xe^x", "1/x", "0"], "e^x"),
("Integral of sin x?", ["-cos x", "cos x", "sin x", "tan x"], "-cos x"),
("Variance formula uses?", ["Mean", "Median", "Mode", "Range"], "Mean"),
("Cosecθ=?", ["1/sinθ", "1/cosθ", "tanθ", "cotθ"], "1/sinθ"),
("Orthogonal vectors dot product?", ["0", "1", "-1", "∞"], "0"),
("If determinant=0 matrix is?", ["Singular", "Identity", "Unit", "Zero"], "Singular"),
("Derivative of 1/x?", ["-1/x2", "1/x", "x", "0"], "-1/x2"),
("Area of circle?", ["πr2", "2πr", "πd", "r2"], "πr2"),
("If tanθ=1 θ=?", ["45°", "30°", "60°", "90°"], "45°"),
("Log identity log(ab)?", ["log a + log b", "log a - log b", "log a × log b", "log a/log b"], "log a + log b"),
("Scalar product formula?", ["A·B=|A||B|cosθ", "A×B", "A+B", "A-B"], "A·B=|A||B|cosθ"),
("Sum of angles triangle?", ["180°", "360°", "90°", "270°"], "180°"),
("Derivative of √x?", ["1/(2√x)", "√x", "2√x", "x"], "1/(2√x)")
]



# =========================
# STRUCTURE FOR TABBED UI
# =========================

questions = {
    "Physics": [
        {
            "question": q[0],
            "options": q[1],
            "answer": q[2]
        } for q in physics_data
    ],

    "Chemistry": [
        {
            "question": q[0],
            "options": q[1],
            "answer": q[2]
        } for q in chemistry_data
    ],

    "Mathematics": [
        {
            "question": q[0],
            "options": q[1],
            "answer": q[2]
        } for q in math_data
    ]
}

print("Physics:", len(questions["Physics"]))
print("Chemistry:", len(questions["Chemistry"]))
print("Mathematics:", len(questions["Mathematics"]))

print("Total Questions:", sum(len(questions[subject]) for subject in questions))