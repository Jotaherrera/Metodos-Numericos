roots = []
counters = []

# Get equation entry
eqVar, degree = self.getEntry()

bigCount = 0
while len(roots) < degree:
            bigCount += 1
            counter = 0

            # Generating random number
            x1 = 0
            xI = self.getSeed(roots)

            # Initial replacing
            eq = eqVar.replace("xI", str(xI))
            if xI >= 0:  # if xI is positive or zero
                while True:
                    if eval(eq) > 0:
                        counter += 1
                        x1 = xI - 0.001
                        xI = x1
                        eq = eqVar.replace("xI", str(xI))
                    elif eval(eq) < 0:
                        counter += 1
                        x1 = xI + 0.001
                        xI = x1
                        eq = eqVar.replace("xI", str(xI))

                    if abs(eval(eq)) <= 0.001:
                        self.verifyRoots(roots, counters, xI, counter)
                        break

                    if counter > 1000:
                        break

            else:  # if xI is negative
                while True:
                    if eval(eq) > 0:
                        counter += 1
                        x1 = xI + 0.001
                        xI = x1
                        eq = eqVar.replace("xI", str(xI))
                    elif eval(eq) < 0:
                        counter += 1
                        x1 = xI - 0.001
                        xI = x1
                        eq = eqVar.replace("xI", str(xI))

                    if abs(eval(eq)) <= 0.001:
                        self.verifyRoots(roots, counters, xI, counter)
                        break

                    if counter > 1000:
                        break
            if bigCount > 200:
                break
        self.cleanArray(roots, 0.1)
        self.giveAnswers(
            self.tanteoOutput, self.tanteoIterationsOutput, roots, counters
        )
        return roots