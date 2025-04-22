# Overrides & Customization

# Text overrides

Table Of Contents

- [Applying the Text Change](https://www.peepso.com/knowledgebase/change-text-in-peepso/#0-toc-title)
- [Adding More Changes](https://www.peepso.com/knowledgebase/change-text-in-peepso/#1-toc-title)

Have you ever wonder how to change just a little piece of text within PeepSo? We know you are.

Sometimes that pesky “*Say whats is on your mind…*” in postbox just don’t cut it and you really want to change it to something else. Like “*Send the rocket to Jupiter…*” or “*White House is in Washington…*” (we don’t know why would you want to do that but it’s possible)

Plugin translators have been doing just that for decades using translations files.

Stop there. We are aware you don’t need a translation *per se,* but what is a translation if not a text change?

In this article, we will use [PoEdit](https://poedit.net/) application for macOS, but the same software is available for Windows and Linux

Once you download and install PoEdit, open the application and select “Create New Translation”

![](https://www.peepso.com/wp-content/uploads/2019/04/poedit-start.png)

You might be wondering why not selecting “**Translate WordPress theme or plugin**” and you’re right, it will be easier to do so, but you’ll need paid version of PoEdit to do this, so we’ll stick with “**Create New Translation**” in this exercise.

The popup window to select the POT file will now be shown.

PeepSo, as is the case with every other decently coded WordPress plugin use POT files to handle all language strings.

Locate the POT file from which you want to change text and open it.

POT files for plugins are always in this location.

***ROOT/wp-content/plugins/PLUGIN-NAME/language***

**Examples:**

if you want to change the text in PeepSo Foundation plugin, then the location would be:

*– ROOT/wp-content/plugins/peepso-core/language/peepso-core.pot*

If you want to translate Groups plugin, then the location would be

*– ROOT/wp-content/plugins/peepso-groups/language/groupso.pot*

**Note:** Please be 
advised that some plugin names have been changed over the course of 
PeepSo development to better suit or represent the features of a plugin.
 For example, if you want to translate Chat plugin, it is actually 
called **peepso-messages** and it’s language file **msgso.pot**
To avoid conflicts and having to redo all language files, we didn’t change the POT names.

Once you selected the POT file to modify, PoEdit will ask you what language you want to translate file to.

Assuming you want to change the text for default WordPress language 
choose the English (United States) as shown in the picture bellow.

![](https://www.peepso.com/wp-content/uploads/2019/04/poedit-language-select.png)

Press **CMD + F** if you’re on Mac or **CTRL + F** for Windows and Linux to invoke search popup and search for the keyword you want to change. Here we want to change “*Say whats is on your mind…*” so we will search for keyword “**mind**“.

Press “**Next**” until you find it.

![](https://www.peepso.com/wp-content/uploads/2019/04/poedit-search.png)

In the Translation box, enter your translation for this string

![](https://www.peepso.com/wp-content/uploads/2019/04/poedit-translate.png)

Save the file as **peepso-core-en_US.po** (remember the location where you save them. We will need these files soon)

**Note 1**: If you change other files, like **picso.pot**, **friendso.pot** or **groupso.pot** then you need to name them **picso-en_US.po**, **friendso-en_US.po,** **groupso-en_US.po** and so on

**Note 2:** The file must be saved using **po** extension. There is no typo here.

PoEdit will now create two files

1. peepso-core-en_US.po
2. peepso-core-en_US.mo

## Applying the Text Change

Now that we have our files ready, take them both and copy to following location:

***ROOT/wp-content/languages/plugins/***

If this directory does not exist yet, create it manually

And will you look at that, we just changed the text in the postbox!

![](https://www.peepso.com/wp-content/uploads/2019/04/language-override-effect.png)

## Adding More Changes

To add more changes, edit the newly created **po** file and save to create new **mo** “translation”

# Template overrides

Table Of Contents

- [How to Find The Right File to Override?](https://www.peepso.com/knowledgebase/template-override/#0-toc-title)
    - [Template Overrides Within Current Theme](https://www.peepso.com/knowledgebase/template-override/#1-toc-title)
    - [Template Override Within PeepSo Overrides Folder](https://www.peepso.com/knowledgebase/template-override/#2-toc-title)

This
 article is for advanced users not afraid to go beyond configuration 
switches in WordPress backend, but it’s written in such manner that 
novice users with no previous experience with overrides can easily 
understand it.

This document will show you how to create overrides for PeepSo 
templates. This method works on all PeepSo plugins and there are two 
ways to achieve this customization. We will explain them both, but 
before proceeding, you will need to know few things.

- Every PeepSo plugin have **templates** directory where
templates that show the functionalities are stored. This is how most
well-coded WordPress plugins work to ensure maximum compatibility with
almost any theme you can imagine, and this is why PeepSo is out of the
box compatible with so many WordPress themes.
- We sometimes update our template files to accommodate new features
or fix bugs. There is no way to add new feature if we don’t show it
through template file, and to show it, template file must be updated.
This may lead to discrepancy in features because if you modify the
template file that has the new feature in newest version, then you must
update your override file to actually see this new feature.

## How to Find The Right File to Override?

This can be daunting task if you’re not familiar with theme 
overrides, but once you understand the fundamentals, it becomes 
ridiculously easy.

We already mentioned every PeepSo plugin have **templates** directory where it stores the template files.

Lets try together, to find the right file which will allow us to modify the cover area in the profile

![](https://www.peepso.com/wp-content/uploads/2019/04/profile-admin-cover.png)

Depending on what browser you use, this first step might be 
different, but only in the way it’s presented. The logic behind it is 
absolutely the same.

We are using Firefox Developer Edition in this exercise, but you can use any browser that have Inspector tools built in.

Right click on the area you want to change and click “Inspect Element”

![](https://www.peepso.com/wp-content/uploads/2019/04/inspect-element.png)

Once clicked, the following screen will show up, highlighting the entire area you chose with the right click

![](https://www.peepso.com/wp-content/uploads/2019/04/inspected-element.png)

Our browser did half of the job already. We see that this particular div is styled through **ps-focus js-focus ps-js-focus ps-js-focus–1** selectors.

Now lets fire up our favorite code editor and search the template files for this selectors.

We are using [Brackets](http://brackets.io/) but you can use any editor of your choice as long as it has *Find in files* option

Search with *Find -> Find in files* option with this query

**<div class=”ps-focus**

The search yielded some results

![](https://www.peepso.com/wp-content/uploads/2019/04/search-result-brackets.png)

Lets analyze the result.

There are 51 matches in 5 files. So we already narrowed down our search to 5 files.

Do we need to edit the file which shows the content when user has no access? Nope? Not really.

How about profile options or profile menu? Nope. Group header? Heck no…

So we are down to the “**focus.php**” which looks most suspicious. And yes, you are right, that is the correct file to override.

We will us it as an example in further exercises.

### Template Overrides Within Current Theme

This is probably the most common way to override the PeepSo template files

Continuing our exercise with **focus.php** copy it from:

*ROOT/wp-content/plugins/peepso-core/templates/profile*

to

*ROOT/wp-content/themes/YOUR-THEME/peepso/profile*

### Template Override Within PeepSo Overrides Folder

Alternatively, you can use PeepSo overrides folder to copy the focus.php from

*ROOT/wp-content/plugins/peepso-core/templates/profile*

to

PeepSo 2.x: *ROOT/wp-content/peepso/overrides/templates/profile*PeepSo 3.0.0.0 or later: *ROOT/wp-content/peepso/custom/templates/profile*

**Note:** if this is your first time creating overrides, these folders may not exist and you’ll have to create them manually

# Image overrides

Table Of Contents

- [Video Tutorial](https://www.peepso.com/knowledgebase/assets-overrides-customizing-peepso-images/#0-toc-title)
- [How to Make This Happen?](https://www.peepso.com/knowledgebase/assets-overrides-customizing-peepso-images/#1-toc-title)

Making
 a community your own has never been easier. PeepSo avatars, profile 
covers and all other images are great but they are not perfect fit for 
every community type. What if you could change the default avatars, 
default covers, and many other default images? Yes, you can. And you can
 do it in such way to preserve them when you update PeepSo.

## Video Tutorial

## How to Make This Happen?

It is really simple.

1. Go to *ROOT/wp-content/plugins/peepso-core/assets* directory
2. Copy the folder *images* and paste it into *ROOT/wp-content/peepso/custom/*
3. Start editing files found in *ROOT/wp-content/peepso/custom/images*

If you use  PeepSo 2 or PeepSo 1, 
folder structure is slightly different and the override folder is called
 “overrides”. In step 2, simply use *ROOT/wp-content/peepso/overrides* instead.

Note: If override folder structure does not exist, create the needed folders manually.

That’s really it.

Please bare in mind though, that you need to preserve the file names and folder structure within newly created override.

If you change the file name, or move the images around from subfolders, they will not work.

# Email overrides

Table Of Contents

- [Solution 1; Backend Configuration](https://www.peepso.com/knowledgebase/email-override/#0-toc-title)
- [Solution 2; Template override](https://www.peepso.com/knowledgebase/email-override/#1-toc-title)

One 
of the most common brand identity questions are related to the design of
 emails that have been generated by PeepSo and dispatched to web server 
to send them to end user.

These emails are by default very minimalistic and contain only basic information.

![](https://www.peepso.com/wp-content/uploads/2019/07/email-register.png)

So how to change the color scheme, maybe add an image to reflect your brand?

The solutions are rather simple, but require a basic knowledge of HTML and CSS so you can actually design your email templates.

## Solution 1; Backend Configuration

PeepSo allows for complete change of the email HTML template in the backend configuration.

Go to *WP Admin -> PeepSo -> Configuration -> Notifications* and scroll down to the “Emails” section until you find the options to override an entire HTML

![](https://www.peepso.com/wp-content/uploads/2019/07/email-visible.png)

Simply copy and paste your custom email HTML into the “Override 
entire HTML” box and emails created with PeepSo will follow your new 
design.

Plese note, you can use the tags below in your template.

- {email_contents} – e-mail contents ****
- {unsubscribeurl} – URL of the user notification preferences ****
- {currentuserfullname} – full name of the recipient
- {useremail} – e-mail of the recipient
- {sitename} – the name of your site
- {siteurl} – the URL of your site

Tags marked with an asterisk are required to be included 
in the email template. Bellow is the example of default template and the
 used tags.

![](https://www.peepso.com/wp-content/uploads/2019/07/Default-Email-Template.png)

The template code can be found below. You can modify it in any way 
you like and paste it in the designated place. Remember to keep the 
required tags.

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2323343)

2.25 KiB

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61

`<!-- email sent to new users upon registration --><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">	<head>		<meta name="viewport" content="width=device-width"/>		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>		<title></title>		<style type="text/css">			a {				color: #00b0ff;				text-decoration: none;			}			a:hover,			a:focus {				color: #0092D4;			}		</style>	</head>	<body bgcolor="#ebedf0">		<div style="background-color: #ebedf0;">			<center style="background-color: #ebedf0;">				<table width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width: 750px; font-family: Arial, Helvetica, sans-serif; margin: 0; padding-top: 50px; padding-bottom: 50px;">					<tr>						<td style="padding:30px; background: #fff; border-bottom:1px solid #eee;">							<table width="100%" cellpadding="0" cellspacing="0" border="0" style="">								<tr>									<td style="font-size: 18px; text-align:center;">										<!-- HEADER CONTENT -->										<h3 style="color: #00b0ff; margin: 0; padding: 0; font-size: 26px; line-height: 30px;">    <a href="{siteurl}" style="text-decoration: none; color: #00b0ff;">{sitename}</a></h3>									</td>								</tr>							</table>						</td>					</tr>					<tr>						<td style="background-color: #fff; border-bottom: 1px solid #eee; border-top: 0; margin: 0;">							<!-- CONTENT -->							<div style="font-size: 14px; line-height: 20px;color: #333;padding:30px;">								{email_contents}
							</div>						</td>					</tr>					<tr>						<td style="background-color: #333538; border-top: 0; padding: 30px; margin: 0; text-align:center;">							<!-- FOOTER CONTENT -->							<p style="margin:0; color: #80848a; font-size: 12px;">This email was sent to {currentuserfullname} ({useremail}).</p><p style="margin:0; margin-top:10px; color: #62676e; font-size: 12px;">If you do not wish to receive these emails from {sitename}, you can <a href="{unsubscribeurl}">manage your preferences</a> here.</p><p style="margin:0; margin-top:10px; color: #62676e; font-size: 12px;">Copyright (c) {year} {sitename}</p>						</td>					</tr>				</table>			</center>		</div>	</body></html>`

## Solution 2; Template override

We already wrote about [template overrides](https://www.peepso.com/documentation/template-override/) and how they work, so we won’t try to re-invent the wheel one more time.

If you’re not sure how template overrides work, we strongly suggest you 
to read the documentation about it. It can apply to any other PeepSo 
template not just emails, and can really be a little extra step that you
 have to do to give your site a personal touch or unique visual 
identity.

To override the PeepSo-generated emails, copy these three (3) files:

- *ROOT/wp-content/plugins/peepso-core/templates/general/email.php*
- *ROOT/wp-content/plugins/peepso-core/templates/general/email-header.php*
- *ROOT/wp-content/plugins/peepso-core/templates/general/email-footer.php*

Paste these files into *ROOT/wp-content/peepso/overrides/templates/general*

Since PeepSo 3, folder structure has been changed and the override folder is now called “custom”. Simply use *ROOT/wp-content/peepso/custom/templates/general* instead.

Note: If override folder structure does not exist, create the needed folders manually.

Once files are copied to the override folder, you can start customizing them to suit your desired visual identity.

# CSS overrides

Table Of Contents

- [PeepSo custom.css Within A Current Theme](https://www.peepso.com/knowledgebase/css-overrides/#0-toc-title)
- [PeepSo style.css Within Content Overrides](https://www.peepso.com/knowledgebase/css-overrides/#1-toc-title)
- [Add The Changes to Additonal CSS Within WordPress Customizer](https://www.peepso.com/knowledgebase/css-overrides/#2-toc-title)
- [Importance of !important Tag](https://www.peepso.com/knowledgebase/css-overrides/#3-toc-title)
- [Example CSS Override File](https://www.peepso.com/knowledgebase/css-overrides/#4-toc-title)

When 
we designed PeepSo, we wanted to be sure that it always looked great. So
 we gave it a completely consistent look. Whatever theme you’re using, 
you’ll get PeepSo exactly the way we designed it.

However, we understand that people want to customize PeepSo, perhaps to tweak the colors so that they better match a theme.

There are several ways to achieve this customization. This article describes them all.

## PeepSo custom.css Within A Current Theme

If you want to do overrides this way, the CSS file should be placed in the */peepso/* directory in the parent directory of your WordPress theme or */peepso3/* directory if you’re using PeepSo 3.x

**Example:**

PeepSo 2.x: *ROOT/wp-content/themes/YOUR_THEME/peepso/*PeepSo 3.x: *ROOT/wp-content/themes/YOUR_THEME/peepso3/*

Inside that directory place the “**custom.css**” file.

It is absolutely required that file must be named “**custom.css**”

**Final custom.css override path is:**

*PeepSo 2.x: ROOT/wp-content/themes/YOUR_THEME/peepso/custom.cssPeepSo 3.x: ROOT/wp-content/themes/YOUR_THEME/peepso3/custom.css*

**Note:** Be aware 
that upgrading the theme might remove this file. So do keep a backup of 
it and keep it up to date if you want to do overrides that way.

## PeepSo style.css Within Content Overrides

Not to worry about losing changes upon upgrading your theme you can 
also put your override file in the PeepSo overrides directory.

**Example:**

PeepSo 2.x:*ROOT/wp-content/peepso/overrides/css/*PeepSo 3.x: *ROOT/wp-content/peepso/custom/css/*

Name the file: **style.css**

**The full path to style.css override will be**

*PeepSo 2.x: ROOT/wp-content/peepso/overrides/css/style.css 
PeepSo 3.x: ROOT/wp-content/peepso/custom/css/style.css*

## Add The Changes to Additonal CSS Within WordPress Customizer

If you don’t need the full override file, you can always place your changes in Additional CSS box through WordPress Customizer.

Go to *WP Admin -> Appearance -> Customize*

Every theme should have the panel where you can add Additional CSS

## Importance of !important Tag

Sometimes the the CSS override won’t work without !important tag. 
This is because the way CSS (Cascading Style Sheet) is designed.

Cascading Style Sheets, well, they cascade, and last loaded value is always in effect.

**Example:**

First loaded CSS file has this class

`.div {background-color: black !important;}`

Last loaded CSS file has this class

`.div {background-color: white;}`

If there were no **!important** tag in the first loaded CSS, the background would be white because value will cascade to the last loaded one. But **!important** tag forced it to remain black.

With that in mind, if your CSS overrides don’t work, try to force them by adding an **!important** tag to the values for every parameter.

## Example CSS Override File

`/*=== TOOLBAR RELATED COLORS ===*/
/* Wrapping PeepSo main menu with all available plugin pages and notifications */
.ps-toolbar {
background-color: #949494;
}
/* Regular link style in desktop toolbar */
.ps-toolbar__menu > span > a,
.ps-toolbar__notifications > span > a {
color: #1B1B1B !important;
}
/* Primary toolbar links on hover */
.ps-toolbar__menu > span > a:hover,
.ps-toolbar__notifications > span > a:hover,
.ps-toolbar__menu > span > a:focus,
.ps-toolbar__notifications > span > a:focus {
background-color: rgba(0,0,0, .05);
}`

You can also find helpful info in the following articles:

- [**Using The Code Snippets In Website Development**](https://www.peepso.com/using-the-code-snippets-in-website-development/)
- [**Taming CSS Elements With Dev Tools**](https://www.peepso.com/taming-css/)

# Snippet: Hide Header Search For Guests

Table Of Contents

- [Overview](https://www.peepso.com/knowledgebase/snippet-hide-header-search-for-guests/#0-toc-title)
- [How To Apply This Snippet?](https://www.peepso.com/knowledgebase/snippet-hide-header-search-for-guests/#1-toc-title)

**Note:**
 this is the custom code change and as such is not officially supported 
by PeepSo team. You should create the full backup of your site before 
applying custom codes.

### Overview

This snippet will allow you to hide the header search for people who are not logged in.

![](https://www.peepso.com/wp-content/uploads/2021/04/snippet-header-search-1024x112.png)

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104686)

89 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4

`/* hide search for guests */body:not(.logged-in) .gc-header__search {  display: none;}`

### How To Apply This Snippet?

- **Method 1 (Manually)** – Open the WordPress Admin
Panel and navigate to “Appearance -> Customize”. Once WordPress
Customizer is open, expand the Custom CSS panel and copy the snippet to
it.
- **Method 2 (Trough plugin)** – NOT SUPPORTED! Since this is a CSS change, you can’t use the plugins like [Code Snippets](https://wordpress.org/plugins/code-snippets/) to add it. It must be installed manually.

# Snippet: Hiding Image Upload In Messages

Table Of Contents

- [Overview](https://www.peepso.com/knowledgebase/hiding-image-upload-in-messages/#0-toc-title)
- [How To Apply This Snippet?](https://www.peepso.com/knowledgebase/hiding-image-upload-in-messages/#1-toc-title)

**Note:**
 this is the custom code change and as such is not officially supported 
by PeepSo team. You should create the full backup of your site before 
applying custom codes.

### Overview

This snippet will allow you to hide the option to upload images in the chat as shown in the screenshot bellow;

![](https://www.peepso.com/wp-content/uploads/2021/04/snippet-hide-image-upload.png)

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2103910)

191 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7

`/*hide image upload in messages*/#postbox-message .ps-icon.gcis.gci-camera:before {  display: none;}#postbox-message .ps-dropdown__menu .ps-postbox__type:nth-child(2) {  display: none;}`

### How To Apply This Snippet?

- **Method 1 (Manually)** – Open the WordPress Admin
Panel and navigate to “Appearance -> Customize”. Once WordPress
Customizer is open, expand the Custom CSS panel and copy the snippet to
it.
- **Method 2 (Trough plugin)** – NOT SUPPORTED! Since this is a CSS change, you can’t use the plugins like [Code Snippets](https://wordpress.org/plugins/code-snippets/) to add it. It must be installed manually.

# Other CSS snippets I didn’t copy over

- [Snippet: Hide Header Search For Guests](https://www.peepso.com/knowledgebase/snippet-hide-header-search-for-guests/)
- 
- [Snippet: Hiding Image Upload In Messages](https://www.peepso.com/knowledgebase/hiding-image-upload-in-messages/)
- 
- [Snippet: Pin to Top post – Legacy look (from PeepSo 2)](https://www.peepso.com/knowledgebase/snippet-pin-to-top-post-legacy-look-from-peepso-2/)
- 
- [Snippet: Change or remove landing template transparent image color](https://www.peepso.com/knowledgebase/change-or-remove-landing-template-transparent-image-color/)
- 
- [Snippet: Change PeepSo postbox placeholder text color](https://www.peepso.com/knowledgebase/snippet-change-peepso-postbox-placeholder-text-color/)
- 
- [Snippet: Custom icon for Chat](https://www.peepso.com/knowledgebase/snippet-custom-icon-for-chat/)
- 
- [Snippet: Display PeepSo Navigation Bar Only On Mobile](https://www.peepso.com/knowledgebase/snippet-display-peepso-navigation-bar-only-on-mobile/)
- 
- [Snippet: Hide Group Avatar](https://www.peepso.com/knowledgebase/snippet-hide-group-avatar/)
- 
- [Snippet: Show PeepSo postbox options](https://www.peepso.com/knowledgebase/snippet-show-peepso-postbox-options/)
- 
- [Snippet: Multi-Colored Hashtags In The Hashtags Widget](https://www.peepso.com/knowledgebase/snippet-multi-colored-hashtags-in-the-hashtags-widget/)
- 
- [Snippet: Hide PeepSo Stream Ad On Profile / Groups](https://www.peepso.com/knowledgebase/snippet-hide-peepso-stream-ad-on-profile-groups/)
- 
- [Snippet: Change Notifications Bubble Color](https://www.peepso.com/knowledgebase/snippet-change-notifications-bubble-color/)
- 
- [Snippet: Hide Stream Filters Warning](https://www.peepso.com/knowledgebase/snippet-hide-stream-filters-warning/)
- 
- [Snippet: Hide Media Subtitle](https://www.peepso.com/knowledgebase/snippet-hide-media-subtitle/)
- 
- [Snippet: Custom Title Color For Gecko Widgets](https://www.peepso.com/knowledgebase/snippet-custom-title-color-for-gecko-widgets/)
- 
- [Snippet: Color Change For Input Fields On The Gecko Landing Page](https://www.peepso.com/knowledgebase/color-change-for-input-fields-on-the-gecko-landing-page/)
- 
- [Snippet: Hide poll item votes](https://www.peepso.com/knowledgebase/snippet-hide-poll-item-votes/)
- 
- [Snippet: Force Font Family](https://www.peepso.com/knowledgebase/force-font-family/)
- 
- [Snippet: Gecko mobile menu custom color](https://www.peepso.com/knowledgebase/snippet-gecko-mobile-menu-custom-color/)
- 
- [Snippet: Hide Text From Moods](https://www.peepso.com/knowledgebase/snippet-hide-text-from-moods/)
- 
- [Snippet: Change hashtag background in PeepSo postbox](https://www.peepso.com/knowledgebase/snippet-change-hashtag-background-in-peepso-postbox/)
- 
- [Snippet: PeepSo Navigation Bar Custom Color](https://www.peepso.com/knowledgebase/snippet-peepso-navigation-bar-custom-color/)
- 
- [Snippet: Album Display Fix For Third-party Themes](https://www.peepso.com/knowledgebase/snippet-album-display-fix-for-third-party-themes/)
- 
- [Snippet: Custom colors for registration form when using Gecko dark template](https://www.peepso.com/knowledgebase/snippet-custom-colors-for-registration-form-when-using-gecko-dark-template/)
- 
- [Snippet: Hide footer on mobile view](https://www.peepso.com/knowledgebase/hide-footer-on-mobile-view/)
- 
- [Snippet: Hide Cover Options](https://www.peepso.com/knowledgebase/snippet-hide-cover-options/)
- 
- [Snippet: Change Notifications Colors](https://www.peepso.com/knowledgebase/snippet-change-notifications-colors/)
- 
- [Snippet: Remove Login Box From Landing Page](https://www.peepso.com/knowledgebase/snippet-remove-login-box-from-landing-page/)
- 
- [Snippet: Hide Avatar Change Option](https://www.peepso.com/knowledgebase/snippet-hide-avatar-change-option/)
- 
- [Snippet: Hide Profile Progress Bar](https://www.peepso.com/knowledgebase/snippet-hide-profile-progress-bar/)
- 
- [Snippet: Change notifications background to round shape](https://www.peepso.com/knowledgebase/snippet-change-notifications-background-to-round-shape/)
- 
- [Snippet: Change Position Of New Message Popup Window](https://www.peepso.com/knowledgebase/snippet-change-position-of-new-message-popup-window/)
- 
- [Snippet: Display Members Search Filters](https://www.peepso.com/knowledgebase/snippet-display-members-search-filters/)
- 
- [Snippet: Changing Input Colors On The Registration Page](https://www.peepso.com/knowledgebase/snippet-changing-input-colors-on-the-registration-page/)
- 

[Snippet: Chanage Landing Form Button Colors](https://www.peepso.com/knowledgebase/snippet-chanage-landing-form-button-colors/)

# Hooks

## **Filter: oEmbed**

## Filter: oEmbed

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-enable_oembed/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-enable_oembed/#1-toc-title)

| **Hook** | `peepso_enable_oembed`
 |
| --- | --- |
| **Plugin** | PeepSo Foundation |
| **Since** | 2.7.7 |
| **Status** | Active |
| **Args** | `bool
string` |

## Description

This filter  can be used to **enable or disable oEmbed** in the `PeepSoEmbed`
 class (it’s enabled by default). When oEmbed is disabled, PeepSo will 
not attempt to embed links via the oEmbed endpoints and instead will 
immediately fall back to Open Graph based discovery.

You can use `peepso_enable_oembed` to completely disable 
oEmbed discovery, or use some rules. The most common use for this would 
be disabling oEmbed for certain domains –  the `$url` argument is provided in that case.

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104773)

218 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8
9
10

`// Disable oEmbed discovery for *i.imgur.com*add_filter('peepso_enable_oembed', function($enabled, $url) {    
    if(stristr($url,'i.imgur.com')) {        $enabled = FALSE;    }    return $enabled;    
},1,2);`

## Action: new reported content

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/action-report-created/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/action-report-created/#1-toc-title)

| **Hook** | `peepso_after_login_form`
 |
| --- | --- |
| **Plugin** | PeepSo Foundation |
| **Since** | 1.8.2 |
| **Status** | Active |
| **Args** | `array` |

## Description

Fires after a new report is filed, passes the array used to perform the insert.

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104718)

601 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8
9
10
11
12

`// send an email when a report is madeadd_action('peepso_action_report_create', function(array $args) {    // module_id identifies which part of PeepSo "owns" the content_id (activity, photo, profile)    $content_module_id = isset($args['rep_module_id']) ? $args['rep_module_id'] : NULL; 
    $content_id = $args['rep_external_id']; 
    // report reason    $reason = isset($args['rep_reason']) ? $args['rep_reason'] : NULL;    
 
    $PeepSoUser = PeepSoUser::get_instance();   
    mail('admin@example.com', 'New report from ' . $PeepSoUser->get_firstname(),'New content reported');}, 10, 1);`

## Filter: country list

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-country-list/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-country-list/#1-toc-title)

| **Hook** | `peepso_filter_countries` |
| --- | --- |
| **Plugin** | PeepSo Foundation |
| **Since** | 2.0.0 |
| **Status** | Active |
| **Args** | `array(string=>string)` |

## Description

PeepSo is using the [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) standard for country codes. If you wish to remove, rename, add items to this list, you can use this filter.

**The final country list will be sorted alphabetically.**

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104731)

186 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8

`/** Removing a country* Not that many people live in Antarctica*/add_filter('peepso_filter_countries', function($countries) {    unset($countries['AQ']);    return $countries;});`

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104732)

326 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8
9
10

`/** Adding a country* The original array uses two-character keys according to the alpha-2 standard, but you can use any strings.* Live long and prosper*/add_filter('peepso_filter_countries', function($countries) {    $countries['KLG'] = 'The Klingon Empire';    $countries['VUL'] = 'Vulcan';    return $countries;});`

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104725)

165 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8

`/** Renaming a country* Poland strong!*/add_filter('peepso_filter_countries', function($countries) {    $countries['PL'] = 'POLSKA';    return $countries;});`

## Filter: community navigation

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-community-navigation/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-community-navigation/#1-toc-title)
- [Screenshot](https://www.peepso.com/knowledgebase/filter-community-navigation/#2-toc-title)

| **Hook** | `peepso_navigation`
 |
| --- | --- |
| **Plugin** | PeepSo Foundation |
| **Since** | 1.8.5 |
| **Status** | Active |
| **Args** | `array` |

## Description

This filter is used to build the

- desktop toolbar
- desktop notification area
- mobile hamburger menu
- mobile notification area
- “community links” section of the profile widget

You can append a new 
key-value pair to the result array. Key must be an unique string 
identifying your plugin. Value is an array with the following keys:

- 
    - **required**
        - `href` – the URL of the link
        - `label` – the text label
        - `icon` – CSS class of an icon. Needs to work both as `<i>` and `<span>` and is needed for `icon-only` and the widget
    - 
    - 
    - 
    - **optional**
        - `class` – CSS class of the parent element
        - `icon-only` – whether the link should be just an icon – label is then ignored
        - `count` – count of notifications
    - 
    - 
    - 

Each link added to the stack is also required to have five TRUE/FALSE flags deciding which area it should render in:

- `primary`
- `secondary`
- `mobile-primary`
- `mobile-secondary`
- `widget`

**See screenshot below for better explaination**

Depending on TRUE/FALSE value
 of each key, the link will be rendered in the given area. Third parties
 are generally advised not to use the “secondary” positions, because the
 layout will most likely break.

With this filter it is 
possible to have different links in the toolbar and the widget, although
 for consistency a link should always show both in the primaries and the
 widget – with optional admin switches to disable them.

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104756)

748 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

`// Add "hello" menu to primary PeepSo Community linksadd_filter('peepso_navigation', function($navigation){    $navigation['hello'] = array(   // this key needs to be unique to your plugin      'href' => '/hello',           // you probably want to get the permalink programatically      'label' => __('Hello','hello'),      'icon'  => 'icon-hello',      // CSS needs to work both as <i> and <span>      'primary'           => TRUE,  // Main toolbar      'secondary'         => FALSE, // Notification area      'mobile-primary'    => TRUE,  // Mobile hamburger menu      'mobile-secondary'  => FALSE, // Mobile notification area      'widget'            => TRUE,  // Profile widget "community links"    );    return ($navigation);});`

## Screenshot

Elements marked in red are managed by `peepso_navigation`, yellow marks `peepso_navigation_profile`. **Mobile** view on the left, **desktop** view on the right

peepso_navigation & peepso_navigation_profile

![](https://www.peepso.com/wp-content/uploads/2020/04/Screenshot_2017-08-14_14.21.58-1024x745.png)

## Filter: photo thumbnail sizes

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-photo-thumbnail-sizes/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-photo-thumbnail-sizes/#1-toc-title)

| **Hook** | `peepso_filter_photos_thumb_settings`
 |
| --- | --- |
| **Plugin** | PeepSo Photos |
| **Since** | 1.10.4 |
| **Status** | Active |
| **Args** | `array` |

## Description

Used to modify the size (in pixels) of thumbnails generated by PeepSo Photos.

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104749)

186 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5

`// change the size of big uncropped thumb to 1024add_filter('peepso_filter_photos_thumb_settings', function($thumbs){    $thumbs['l'] = array(1024, 0, FALSE);    return($thumbs);});`

## Filter: media upload title & icon

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-media-upload-title-icon/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-media-upload-title-icon/#1-toc-title)

| **Hook** | `peepso_filter_video_action_icon
peepso_filter_video_action_text
peepso_filter_audio_action_icon
peepso_filter_audio_action_text`
 |
| --- | --- |
| **Plugin** | PeepSo Audio & Video |
| **Since** | 2.0.0 |
| **Status** | Active |
| **Args** | `string` |

## Description

When users upload video and 
audio files, the resulting activity title contains an action text, icon 
and user-entered title. The action text and icon are customizable with 
these four filters.

Modify the CSS of the icons to change the icon or hide it completely: `peepso_filter_video_action_icon` – modifies the CSS class of the video icon `peepso_filter_audio_action_icon` – modifies the CSS class of the audio icon

Modify the action text or disable it (with an empty string) `peepso_filter_video_action_text` – modifies the action text on a video post `peepso_filter_audio_action_text` – modifies the action text on an audio post

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104751)

650 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

`// change icon on post containing a video uploadadd_filter('peepso_filter_video_action_icon', function($icon){    return 'ps-icon-youtube-play';});// change action text on post containing a video uploadadd_filter('peepso_filter_video_action_text', function($action){    return __('shared a video', 'peepso-core');});// change icon on post containing an audio uploadadd_filter('peepso_filter_audio_action_icon', function($icon){    return 'ps-icon-headphones';});// change action text on post containing an audio uploadadd_filter('peepso_filter_audio_action_text', function($action){    return __('shared a song', 'peepso-core');});`

## Filter: Stream Ad – allowed HTML

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-advanced-ads-stream-ad-html/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-advanced-ads-stream-ad-html/#1-toc-title)

| **Hook** | `peepso_filter_advads_allowed_html`
 |
| --- | --- |
| **Plugin** | PeepSo Advanced Ads |
| **Since** | 3.2.0.0 |
| **Status** | Active |
| **Args** | `array` |

## Description

Used to modify the list of HTML tags allowed in PeepSo Stream Ad 
type. The argument is an array of strings. There is no validation or 
cleanup, **use only a-z characters** (like *iframe*) and avoid using any special characters like spaces, braces etc.

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/codesnippets/-/snippets/2104796)

186 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5

`// add iframe to supported HTML tags in Advanced Ads PeepSo Stream Ad type add_filter('peepso_filter_advads_allowed_html', function($tags) {    $tags[]='iframe';    return $tags;});`

## Filter: Disable Public Privacy

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-disable-public-privacy/#0-toc-title)
    - [Examples](https://www.peepso.com/knowledgebase/filter-disable-public-privacy/#1-toc-title)

| **Hook** | `peepso_privacy_access_levels`
 |
| --- | --- |
| **Plugin** | PeepSo Foundation |
| **Since** | 1.x |
| **Args** | `string` |

# Description

In this example we will disable the “Public” privacy level which might be irrelevant to some closed communities.

The levels are governed by `peepso_privacy_access_levels` filter.

PeepSo has multiple fallbacks 
in case of missing privacy levels, nevertheless removing things with 
this filter should only be considered on a fresh install. **If anyone already used it** (eg in a post), it might result in some weird results.

## Examples

[**example.php**](https://gitlab.com/PeepSo/Public/HelloWorld/-/snippets/1727592)

161 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6
7

`<?php// Disable Public privacy leveladd_filter('peepso_privacy_access_levels', function($levels){ unset($levels[PeepSo::ACCESS_PUBLIC]); return $levels;});`

## Filter: User name length

## 

Table Of Contents

- [Description](https://www.peepso.com/knowledgebase/filter-user-name-length/#0-toc-title)
- [Examples](https://www.peepso.com/knowledgebase/filter-user-name-length/#1-toc-title)

| **Hook** | `peepso_filter_username_len_max`

`peepso_filter_username_len_min` |
| --- | --- |
| **Plugin** | PeepSo Foundation |
| **Since** | 6.0.4.0 |
| **Status** | Active |
| **Args** | int |

## Description

These filters can be used to control the allowed username length.

## **Examples**

[**Maximum username length.php**](https://gitlab.com/PeepSo/Public/HelloWorld/-/snippets/3612446)

111 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6

`<?php// Maximum username lengthadd_filter('peepso_filter_username_len_max', function($len){	return 10;});`

[**Minimum username length.php**](https://gitlab.com/PeepSo/Public/HelloWorld/-/snippets/3612446)

110 B

![](https://gitlab.com/assets/ext_snippet_icons/logo-88d040ec5541207676259c7d6dd92345e719e117099a26d3a1361ade5bbd2b9c.svg)

1
2
3
4
5
6

`<?php// Minimum username lengthadd_filter('peepso_filter_username_len_min', function($len){	return 5;});`

[Filter: Disable Public Privacy](https://www.peepso.com/knowledgebase/filter-disable-public-privacy/)

# Hooks I didn’t copy over

[Hooks: Groups](https://www.peepso.com/knowledgebase/filter-user-name-length/#)

- [Action: group created](https://www.peepso.com/knowledgebase/action-group-created/)
- [Action: group invitation accepted](https://www.peepso.com/knowledgebase/action-group-invitation-accepted/)
- [Action: group invitation sent](https://www.peepso.com/knowledgebase/action-group-invitation-sent/)
- [Action: group joined](https://www.peepso.com/knowledgebase/action-group-joined/)
- [Filter: group privacy](https://www.peepso.com/knowledgebase/filter-group-privacy/)
- 
    - [Disable Specific Group Privacy](https://www.peepso.com/knowledgebase/disable-specific-group-privacy/)
- 

[Hooks: Posts & Comments](https://www.peepso.com/knowledgebase/filter-user-name-length/#)

- [Filter: enable or disable comment box](https://www.peepso.com/knowledgebase/filter-commentsbox_display/)
- 
    - [Action: like added](https://www.peepso.com/knowledgebase/action-like-added/)
- 

[Hooks: Users](https://www.peepso.com/knowledgebase/filter-user-name-length/#)

- [Action: profile completeness changed](https://www.peepso.com/knowledgebase/action-profile-completeness-changed/)
- [Filter: profile navigation](https://www.peepso.com/knowledgebase/filter-profile-navigation/)
- [Filter: custom cover size](https://www.peepso.com/knowledgebase/filter-cover-sizes-to-delete/)
- [Filter: profile navigation order](https://www.peepso.com/knowledgebase/filter-profile-navigation-order/)
- [Filter: name parts](https://www.peepso.com/knowledgebase/filter-peepso_get_name_parts/)
- [Action: user profile field saved](https://www.peepso.com/knowledgebase/action-user-profile-field-saved/)

[Action: print after login form](https://www.peepso.com/knowledgebase/action-print-after-login-form/)