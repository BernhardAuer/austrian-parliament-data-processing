<a name="readme-top"></a>
<!--
This readme is based on the following template: https://github.com/othneildrew/Best-README-Template
MIT License

Copyright (c) 2021 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BernhardAuer/austrian-parliament-data-processing">
    <img src="https://github.com/BernhardAuer/austrian-parliament-data-processing/assets/40627756/25024a9e-89cc-4141-8d9c-67e1db694c2a" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">parli-info.org</h3>

  <p align="center">
    Website for visualizing austrian's open government data in an appealing, interactive and simple-to-use manner.
    <br />
    <a href="https://github.com/BernhardAuer/austrian-parliament-data-processing"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://parli-info.org">View Website</a>
    ·
    <a href="https://github.com/BernhardAuer/austrian-parliament-data-processing/issues">Report Bug</a>
    ·
    <a href="https://github.com/BernhardAuer/austrian-parliament-data-processing/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
We provide an easy-to-use platform, which lets people discover debates held in the austrian parliament. Our aim is to encourage people's political curiosity by providing truthful information and statistics. Let's discover the interesting world of politics together!

 <!-- Let us reflect our own political positions and initiate further discussions. Furthermore, this tool might could be used  exploring certain topics of austrian politics. -->

 
[![Product Name Screen Shot][product-screenshot]](https://parli-info.org/wortmeldungsarten)
![frame_safari_light (2)](https://github.com/BernhardAuer/austrian-parliament-data-processing/assets/40627756/384ad18b-520f-4851-b59d-407ad3bc2ecb)


#### Our Design Principles
- Privacy protection. This platform does not and will never collect any user related data. We think that political views are a highly personal subject and worthy of protection.
- Free to use, for everyone.
- No advertising, ever.
- Focus on good UX.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* Frontend
  * ![SvelteKit](https://img.shields.io/badge/SvelteKit-FF3E00?style=for-the-badge&logo=Svelte&logoColor=white)
  * ![TailwindCss](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
  * ![DaisyUi](https://img.shields.io/badge/daisyUI-1ad1a5?style=for-the-badge&logo=daisyui&logoColor=white)
* Backend
  * ![asp.net core](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
  * ![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)
  * ![MongoDb](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
* Scraper
  * ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
  * <img src="https://github.com/BernhardAuer/austrian-parliament-data-processing/assets/40627756/7e749444-b9a5-4288-aa97-3746205cae9e" alt="Scrapy" height="25">


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Hosted on
* Frontend
  * Azure Static Web App
  * Azure Function Node.js (SWA managed Function)
* Backend
  * Azure App Service (including managed Domain/DNS/SSL-Cert)
  * MongoDb Atlas (M0 Sandbox)
* Scraper
  * Azure Container Registry
  * Azure Container Apps
* Monitoring
  * Azure Monitor
  * Azure App Insights
 
All Services are running in the Azure Region Westeurope (Netherlands)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/BernhardAuer/austrian-parliament-data-processing.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/BernhardAuer/austrian-parliament-data-processing/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bernhard Auer - auer-bernhard@protonmail.com

Project Link: [https://github.com/BernhardAuer/austrian-parliament-data-processing](https://github.com/BernhardAuer/austrian-parliament-data-processing)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BernhardAuer/austrian-parliament-data-processing.svg?style=for-the-badge
[contributors-url]: https://github.com/BernhardAuer/austrian-parliament-data-processing/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BernhardAuer/austrian-parliament-data-processing.svg?style=for-the-badge
[forks-url]: https://github.com/BernhardAuer/austrian-parliament-data-processing/network/members
[stars-shield]: https://img.shields.io/github/stars/BernhardAuer/austrian-parliament-data-processing.svg?style=for-the-badge
[stars-url]: https://github.com/BernhardAuer/austrian-parliament-data-processing/stargazers
[issues-shield]: https://img.shields.io/github/issues/BernhardAuer/austrian-parliament-data-processing.svg?style=for-the-badge
[issues-url]: https://github.com/BernhardAuer/austrian-parliament-data-processing/issues
[license-shield]: https://img.shields.io/github/license/BernhardAuer/austrian-parliament-data-processing.svg?style=for-the-badge
[license-url]: https://github.com/BernhardAuer/austrian-parliament-data-processing/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: https://github.com/BernhardAuer/austrian-parliament-data-processing/assets/40627756/50ebf8aa-4b73-48b3-8c22-7cb70b833ec2
[tailwindcss]: https://img.shields.io/badge/tailwindcss-0F172A?&logo=tailwindcss&style=for-the-badge&logoColor=FF3E00
[tailwindcss-url]: https://tailwindcss.com/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
