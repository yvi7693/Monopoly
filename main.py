from src.presenter.core import GamePresenter

def main():
    while True:
        presenter = GamePresenter()

        if not presenter.need_restart:
            break



if __name__ == "__main__":
    main()