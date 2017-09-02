class App:
    def __init__(self, name):
        self.name = name

    def main(self):
        return 'Hello {}'.format(self.name)


if __name__ == '__main__':
    app = App('Mr. App')
    print(app.main())
