# Dynamic Download

Very, *very* basic script to download a list of links from a dynamically generated web page.

Developed to aid in downloading from a government data portal that was previously an FTP site, but now a web page with a dynamically generated list of links. 

# Requirements

- Python 3 (with Poetry)
- Docker (with Compose)

## Use

To create a list of URLs from the links on `https://example.com` that contain either `pdf` or `zip`:

    $ poetry install
    $ poetry shell
    $ python3 ./main.py "https://example.com" -x zip pdf

If you do not have the Chrome driver installed, you can use a Docker container to launch the browser and monitor its activity. 

**Apple Silicon users:** modify the `Dockerfile` to switch to the `seleniarm` build. 

Before running `main.py`, start the Docker container:

    $ docker-compose up --build -d

Once the Docker container is running, you can view the browser session at [http://localhost:7900/?autoconnect=1&resize=scale&password=secret](http://localhost:7900/?autoconnect=1&resize=scale&password=secret). 

## Thanks

Thanks to everyone on the Selenium project!
