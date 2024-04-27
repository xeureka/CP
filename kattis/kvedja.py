<!DOCTYPE html>
<html class="" lang="en">
<head>
    <!-- Load sentry as early as possible -->
            <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="https://js.sentry-cdn.com/1ad5e9767ad243d396a93ef40135e743.min.js" crossorigin="anonymous" data-lazy="no"></script>

    <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="module">
        Sentry.onLoad(function() {
            Sentry.init({
                dsn: "https://1ad5e9767ad243d396a93ef40135e743:0f66eac85d88443baa349f5bc2497f28@sentry.io/271015",
                release: "de6b78b990a456a08354d3541e5dda1eda82cc0f",
                environment: "edu",
                whitelistUrls: [
                    /https?:\/\/open\.kattis\.com/                 ],
                ignoreErrors: [
                    "Non-Error exception captured",                     "Non-Error promise rejection captured",                    'ResizeObserver loop limit exceeded'                ],
                ignoreUrls: ['/static\.cloudflareinsights\.com/'],                 autoSessionTracking: false,
                integrations: [                    new Sentry.BrowserTracing(),
                ],
                tracesSampleRate: 0,
                profilesSampleRate: 1.0,
                replaysSessionSampleRate: 0,                 replaysOnErrorSampleRate: 0,                 tracePropagationTargets: ["localhost", /https?:\/\/open\.kattis\.com/],             });
                        Sentry.configureScope((scope) => scope.setTransactionName("user_login"));         })
    </script>

    <meta charset="UTF-8" >
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Log in or sign up for Kattis &ndash; Kattis, Kattis</title>

    <!-- Jquery and Jquery-ui -->
    <link href="/assets/9f95f04f0ab38849a6582527021cc456/jquery-ui-dist/jquery-ui.theme.min.css" rel="stylesheet">
    <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="/assets/9f95f04f0ab38849a6582527021cc456/jquery/dist/jquery.min.js"></script>
    <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="/assets/9f95f04f0ab38849a6582527021cc456/jquery-ui-dist/jquery-ui.min.js"></script>

    <!-- Timezone Cookie -->
    <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="module" src="/js/e92894b739ba9ea948a6c12162ad64dd/modules/timezone.js"></script>

    <!-- Fonts/Icons -->
    <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fortawesome/fontawesome-free/css/all.min.css" rel="stylesheet">

            <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/merriweather/300.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/merriweather/300-italic.css" rel="stylesheet">
            <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/merriweather/400.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/merriweather/400-italic.css" rel="stylesheet">
            <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/merriweather/700.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/merriweather/700-italic.css" rel="stylesheet">
                <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/300.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/300-italic.css" rel="stylesheet">
            <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/400.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/400-italic.css" rel="stylesheet">
            <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/500.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/500-italic.css" rel="stylesheet">
            <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/700.css" rel="stylesheet">
        <link href="/assets/9f95f04f0ab38849a6582527021cc456/@fontsource/ubuntu/700-italic.css" rel="stylesheet">
    
    <!-- DateRangePicker CSS -->
    <link href="/assets/9f95f04f0ab38849a6582527021cc456/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

    <!-- Editable and Select2 -->
    <link href="/assets/9f95f04f0ab38849a6582527021cc456/select2/dist/css/select2.css" rel="stylesheet">

            <link rel="apple-touch-icon-precomposed" sizes="57x57"   href="/images/favicon/apple-touch-icon-57x57.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/images/favicon/apple-touch-icon-114x114.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72"   href="/images/favicon/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/images/favicon/apple-touch-icon-144x144.png">
        <link rel="apple-touch-icon-precomposed" sizes="60x60"   href="/images/favicon/apple-touch-icon-60x60.png">
        <link rel="apple-touch-icon-precomposed" sizes="120x120" href="/images/favicon/apple-touch-icon-120x120.png">
        <link rel="apple-touch-icon-precomposed" sizes="76x76"   href="/images/favicon/apple-touch-icon-76x76.png">
        <link rel="apple-touch-icon-precomposed" sizes="152x152" href="/images/favicon/apple-touch-icon-152x152.png">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-196x196.png" sizes="196x196">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-96x96.png"   sizes="96x96">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-32x32.png"   sizes="32x32">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-16x16.png"   sizes="16x16">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-128.png"     sizes="128x128">
        <link rel="shortcut icon"         href="/images/favicon/favicon.ico">
        <meta name="application-name"                content="Kattis, Kattis">
        <meta name="msapplication-TileColor"         content="#FFFFFF">
        <meta name="msapplication-TileImage"         content="/images/favicon/mstile-144x144.png">
        <meta name="msapplication-square70x70logo"   content="/images/favicon/mstile-70x70.png">
        <meta name="msapplication-square150x150logo" content="/images/favicon/mstile-150x150.png">
        <meta name="msapplication-wide310x150logo"   content="/images/favicon/mstile-310x150.png">
        <meta name="msapplication-square310x310logo" content="/images/favicon/mstile-310x310.png">
    
    <!-- Own CSS -->
    <link rel="stylesheet" href="/css/070c796e05429f4b14a69d73604f6ecb/style.css">
    <style type="text/css">           .logo {
         background-color: ;
     }
          :root {
                      --branding-border: linear-gradient(rgb(240,176,52), rgb(240,176,52));
              }

          div.page-content.clearfix.above-everything.alert.alert-danger { color: #31708f; background: #d9edf7; border-color: #bce8f1; }
div.page-content.clearfix.above-everything.alert.alert-danger div.main-content { padding-bottom: 0; }

         </style>

    <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="text/javascript">
        window.page_loaded_at = new Date();
        jQuery.noConflict();
    </script>

    
</head>

<body class=" l-body_grid"  >





<header class="l-page_header">
    <div class="page_header-arrow_expand_collapse">
        <i class="page_header-arrow_expand_collapse-arrow"></i>
    </div>
    <div class="page_header-wrapper">
        <div class="logo-container">
            <a class="logo-link" href="/" title="Kattis">
                <img class="logo" src="/images/site-logo?v=0a3f6018aacf449381741e45cf0ff6ba" alt="Kattis logo" />
            </a>
            <h4 class="logo-container-text">Kattis</h4>
            <button class="menu_mobile_link" >
                <i class="fas fa-bars menu_mobile_link_icon"></i>
            </button>
            <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="module" src="/js/e92894b739ba9ea948a6c12162ad64dd/pages/master/nav.js"></script>
        </div>
        <div class="branding_border"></div>
        <div class="page_header-content">
            <nav>
                <ul class="main_menu">
                                                                    <li>
                            <a  href="/problems" class="main_menu-item main_menu-item_link  " title="Problems">
                                                                    <i class="fas fa-puzzle-piece main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Problems</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/contests" class="main_menu-item main_menu-item_link  " title="Contests">
                                                                    <i class="fas fa-award main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Contests</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/challenge" class="main_menu-item main_menu-item_link  " title="Challenge">
                                                                    <i class="fas fa-star main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name beta_label">Challenge</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/ranklist" class="main_menu-item main_menu-item_link  " title="Ranklists">
                                                                    <i class="fas fa-trophy main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Ranklists</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/jobs" class="main_menu-item main_menu-item_link  " title="Jobs">
                                                                    <i class="fas fa-suitcase main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Jobs</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/languages" class="main_menu-item main_menu-item_link  " title="Languages">
                                                                    <i class="fas fa-code main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Languages</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/info" class="main_menu-item main_menu-item_link  " title="Info">
                                                                    <i class="fas fa-info main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Info</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="https://support.kattis.com" class="main_menu-item main_menu-item_link  " title="Help">
                                                                    <i class="fas fa-question main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Help</span>
                                                            </a>
                        </li>
                                    </ul>
            </nav>
                            <div class="header_item_margin search-lower">
                    <label for="search_input" class="search-label search-label-right">Search</label>
                    <form id="search_form" method="GET" action="/search" class="search">
                                                    <img src="/images/site/header/logo-empty.png?0bb770=" alt="Kattis Cat" class="search-mascot" />
                                                <input id="search_input" type="search" name="q" class="search-input" placeholder="Search Kattis" />
                        <i id="search_submit" class="fas fa-search search-icon"></i>
                    </form>
                </div>
            
        </div>
    </div>
</header>

<script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="text/javascript">
    jQuery(function($) {
        $('.page_header-arrow_expand_collapse').click(function() {
            $('body').toggleClass('header-collapsed');
        });
    });
</script>

<div class="l-main_area">
    

            <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="module" src="/js/e92894b739ba9ea948a6c12162ad64dd/modules/banner.js"></script>
                                            <div class="banner banner-centered alert-info">
                <button class="banner-dismiss">
                    <i class="fas fa-times"></i>
                </button>
                <div class="banner-section-icon">
                    <i class="fas fa-info-circle banner-icon"></i>
                </div>
                <div class="banner-section-text">
                    <h4 class="banner-title">
                        The page you are trying to access requires you to be logged in.
                    </h4>
                </div>
            </div>
            
    <main class="flex flex-col grow content_padding">
        



<div class="top_bar ">
    <script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" type="module" src="/js/e92894b739ba9ea948a6c12162ad64dd/pages/master/top_bar.js"></script>
    <div class="branding_border"></div>
    
    

    </div>
        
        
    
    

    
    
    
    
    <div class="login-kattis-position">
        <div class="login-kattis">
                        <header class="login-kattis-header">
                <h1>Log in or sign up for Kattis</h1>
            </header>
            <div class="login-content">
                
	<div class="login-methods"><form action="/login/oauth/Azure" method="GET" style="display:inline-block"><button class="azure"><i class="fab fa-windows"></i>Log in with Azure</button></form><br/><form action="/login/oauth/Facebook" method="GET" style="display:inline-block"><button class="facebook"><i class="fab fa-facebook-f"></i>Log in with Facebook</button></form><br/><form action="/login/oauth/Github" method="GET" style="display:inline-block"><button class="github"><i class="fab fa-github"></i>Log in with Github</button></form><br/><form action="/login/oauth/Google" method="GET" style="display:inline-block"><button class="google"><i class="fab fa-google"></i>Log in with Google</button></form><br/><form action="/login/oauth/LinkedIn" method="GET" style="display:inline-block"><button class="linkedin"><i class="fab fa-linkedin-in"></i>Log in with LinkedIn</button></form><br/><form action="/login/email" method="GET" style="display:inline-block"><button class="email" data-cy="login-with-email"><i class="fa fa-envelope"></i>Log in with e-mail</button></form></div>
			<a class="login-methods-more-link" href="/login/more">More login methods</a>
	
            </div>
            <img class="login-cat" src="/images/kattis/judge.png?6dd056=" alt="Kattis mascot"/>
        </div>
    </div>


    </main>

    



    <footer class="l-footer ">
        <span class="text-center text-sm">
        <a href="/info/contact">Contact</a> |
        <a href="https://status.kattis.com">System Status</a> |
        <a rel="terms-of-service" href="/info/tos">Terms of Service</a> |
        <a rel="privacy-policy" href="https://www.kattis.com/policies/privacy_policy.pdf">Privacy Policy</a>
        </span>
    </footer>

</div>



<script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="/assets/9f95f04f0ab38849a6582527021cc456/moment/min/moment.min.js"></script>
<script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="/assets/9f95f04f0ab38849a6582527021cc456/bootstrap-daterangepicker/daterangepicker.js"></script>
<script nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="/assets/9f95f04f0ab38849a6582527021cc456/select2/dist/js/select2.full.min.js"></script>



        <script defer nonce="9c4451b2fbb42d9754e3a64e33939508ea0c2faf43432292af07674ece527973" src="https://status.kattis.com/embed/script.js"></script>
</body>
</html>
