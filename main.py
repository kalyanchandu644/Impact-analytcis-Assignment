from solution import GraduationCeremony
if __name__ == "__main__":
    inputs = [(5, 4), (10, 4), (15, 4)]  #cannot miss 4 or more than 4 classes consecutively so m is always four for our usecase
    for n, m in inputs:
        obj = GraduationCeremony(n, m)
        obj.run()