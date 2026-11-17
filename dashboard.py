<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>PEC Missing Things</title>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

<style>

*{
    box-sizing:border-box;
    margin:0;
    padding:0;
}

body{
    font-family:Arial,Helvetica,sans-serif;
    background:#f3f6fa;
    color:#152238;
}

button{
    border:0;
    cursor:pointer;
    background:#0b4ea2;
    color:white;
    padding:12px 18px;
    border-radius:10px;
    font-weight:bold;
}

button:hover{
    opacity:.9;
}

input,
textarea,
select{
    width:100%;
    padding:13px;
    margin:7px 0;
    border:1px solid #d5dce7;
    border-radius:10px;
    outline:none;
    font-size:15px;
}

textarea{
    min-height:120px;
    resize:vertical;
}

.hidden{
    display:none!important;
}


/* ACCESS PAGE */

#accessPage{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:20px;

    background:
    linear-gradient(
        135deg,
        #071d38,
        #1767a8
    );
}

.access-box{
    width:100%;
    max-width:440px;
    background:white;
    padding:40px;
    border-radius:24px;
    text-align:center;
    box-shadow:0 25px 80px rgba(0,0,0,.3);
}

.logo{
    width:70px;
    height:70px;
    margin:auto;

    display:flex;
    align-items:center;
    justify-content:center;

    background:#0b4ea2;
    color:white;

    border-radius:50%;

    font-weight:bold;
    font-size:22px;
}

.access-box h1{
    margin-top:20px;
    font-size:26px;
}

.access-box h2{
    margin-top:5px;
    color:#0b4ea2;
}

.access-box p{
    margin:15px 0;
    color:#667085;
}

.access-box button{
    width:100%;
}

.error{
    color:#d62828!important;
}


/* HEADER */

header{
    background:white;
    border-bottom:1px solid #e0e5eb;

    padding:17px 5%;

    display:flex;
    justify-content:space-between;
    align-items:center;

    position:sticky;
    top:0;
    z-index:5;
}

.brand h1{
    font-size:21px;
}

.brand p{
    color:#667085;
    font-size:12px;
    margin-top:3px;
}

.header-actions{
    display:flex;
    align-items:center;
    gap:8px;
}

.user-email{
    font-size:12px;
    color:#667085;
}


/* HERO */

.hero{
    width:90%;
    max-width:1100px;

    margin:30px auto 20px;

    padding:35px;

    border-radius:23px;

    background:
    linear-gradient(
        120deg,
        #08264b,
        #146da9
    );

    color:white;

    display:flex;
    justify-content:space-between;
    align-items:center;

    gap:20px;
}

.hero h2{
    font-size:32px;
    margin-bottom:8px;
}

.hero p{
    color:#dcecff;
}

.hero button{
    background:white;
    color:#0b4ea2;
}


/* SEARCH */

.search-area{
    width:90%;
    max-width:1100px;

    margin:auto;

    display:grid;
    grid-template-columns:1fr 250px;

    gap:10px;
}


/* POSTS */

#posts{
    width:90%;
    max-width:1100px;

    margin:25px auto;

    display:grid;

    grid-template-columns:
    repeat(
        auto-fill,
        minmax(270px,1fr)
    );

    gap:20px;
}

.post{
    background:white;

    border:1px solid #e2e7ee;

    border-radius:18px;

    overflow:hidden;

    box-shadow:
    0 8px 25px rgba(0,0,0,.06);
}

.post-image{
    width:100%;
    height:190px;
    object-fit:cover;
}

.post-content{
    padding:18px;
}

.category{
    font-size:11px;
    font-weight:bold;
    color:#0b4ea2;
    text-transform:uppercase;
}

.post-title{
    font-size:20px;
    margin:7px 0;
}

.location{
    font-size:13px;
    color:#667085;
    margin-bottom:10px;
}

.description{
    font-size:14px;
    line-height:1.5;
}

.post-buttons{
    display:flex;
    gap:8px;
    margin-top:15px;
    flex-wrap:wrap;
}

.secondary{
    background:#eaf0f7;
    color:#163c62;
}


/* MODALS */

.modal{
    position:fixed;
    inset:0;

    background:rgba(0,0,0,.65);

    display:flex;
    justify-content:center;
    align-items:center;

    padding:20px;

    z-index:20;
}

.modal-box{
    width:100%;
    max-width:440px;

    background:white;

    border-radius:18px;

    padding:28px;

    position:relative;

    max-height:90vh;

    overflow-y:auto;
}

.large{
    max-width:650px;
}

.close{
    position:absolute;
    right:15px;
    top:10px;

    background:transparent;
    color:#555;

    font-size:28px;

    padding:0;
}

.close:hover{
    background:transparent;
}

.message{
    margin-top:10px;
    color:#0b4ea2;
}

.reply-card{
    background:#f4f7fb;
    border:1px solid #dfe6ef;

    padding:15px;

    border-radius:12px;

    margin-top:10px;
}

.reply-time{
    margin-top:8px;
    font-size:11px;
    color:#667085;
}


/* MOBILE */

@media(max-width:700px){

    header{
        flex-direction:column;
        align-items:flex-start;
        gap:12px;
    }

    .header-actions{
        width:100%;
        flex-wrap:wrap;
    }

    .hero{
        flex-direction:column;
        align-items:flex-start;
        padding:26px;
    }

    .hero h2{
        font-size:27px;
    }

    .search-area{
        grid-template-columns:1fr;
    }

    #posts{
        grid-template-columns:1fr;
    }

}

</style>
</head>


<body>


<!-- ======================================================
     ACCESS PAGE
====================================================== -->

<div id="accessPage">

<div class="access-box">

<div class="logo">
PEC
</div>

<h1>
Prathyusha Engineering College
</h1>

<h2>
Missing Things
</h2>

<p>
Enter the student access code
</p>

<input
id="accessCode"
type="text"
placeholder="Access Code"
>

<button onclick="checkAccess()">
Enter Website
</button>

<p
id="accessError"
class="error">
</p>

</div>

</div>



<!-- ======================================================
     MAIN WEBSITE
====================================================== -->

<div id="mainPage" class="hidden">


<header>

<div class="brand">

<h1>
PEC Missing Things
</h1>

<p>
Prathyusha Engineering College
</p>

</div>


<div class="header-actions">

<span
id="userEmail"
class="user-email">
</span>

<button
id="loginBtn"
onclick="openLogin()">
Login
</button>

<button
id="signupBtn"
onclick="openSignup()">
Create Account
</button>

<button
id="logoutBtn"
onclick="logout()"
class="hidden">
Logout
</button>

</div>

</header>



<section class="hero">

<div>

<h2>
Lost something?
</h2>

<p>
Find lost belongings or help someone recover theirs.
</p>

</div>

<button onclick="openAddPost()">
+ ADD
</button>

</section>



<!-- SEARCH -->

<div class="search-area">

<input
id="searchInput"
type="text"
placeholder="Search missing things..."
oninput="loadPosts()"
>

<select
id="categoryFilter"
onchange="loadPosts()">

<option value="">
All Categories
</option>

<option>
Water bottles
</option>

<option>
Mobile phones
</option>

<option>
ID cards
</option>

<option>
Bags and backpacks
</option>

<option>
Books and notebooks
</option>

<option>
Laptops and tablets
</option>

<option>
Chargers and earphones
</option>

<option>
Keys and keychains
</option>

<option>
Watches and jewellery
</option>

<option>
Money and wallets
</option>

<option>
ATM cards
</option>

<option>
Shoes and personal belongings
</option>

<option>
Sports equipment
</option>

<option>
Other miscellaneous items
</option>

</select>

</div>



<!-- POSTS -->

<div id="posts"></div>


</div>



<!-- ======================================================
     LOGIN / SIGNUP MODAL
====================================================== -->

<div
id="authModal"
class="modal hidden">

<div class="modal-box">

<button
class="close"
onclick="closeModal('authModal')">
×
</button>


<h2 id="authTitle">
Login
</h2>


<form
onsubmit="handleAuth(event)">


<input
id="email"
type="email"
placeholder="Gmail / Email"
required
>


<input
id="password"
type="password"
placeholder="Password"
minlength="6"
required
>


<input
id="name"
type="text"
placeholder="Name (optional)"
class="hidden"
>


<button type="submit">

<span id="authButton">
Login
</span>

</button>

</form>


<button
id="forgotBtn"
onclick="forgotPassword()"
style="
background:transparent;
color:#0b4ea2;
padding:7px;
margin-top:5px;
">

Forgot password?

</button>


<p
id="authMessage"
class="message">
</p>

</div>

</div>



<!-- ======================================================
     ADD POST MODAL
====================================================== -->

<div
id="postModal"
class="modal hidden">

<div class="modal-box large">

<button
class="close"
onclick="closeModal('postModal')">
×
</button>


<h2>
Add Missing Thing
</h2>

<p style="
color:#667085;
margin:8px 0 15px;
">

Do not reveal secret identifying details
of the item publicly.

</p>


<form
onsubmit="createPost(event)">


<input
id="itemTitle"
type="text"
placeholder="Item title"
required
>


<select
id="itemCategory"
required>

<option value="">
Select category
</option>

<option>
Water bottles
</option>

<option>
Mobile phones
</option>

<option>
ID cards
</option>

<option>
Bags and backpacks
</option>

<option>
Books and notebooks
</option>

<option>
Laptops and tablets
</option>

<option>
Chargers and earphones
</option>

<option>
Keys and keychains
</option>

<option>
Watches and jewellery
</option>

<option>
Money and wallets
</option>

<option>
ATM cards
</option>

<option>
Shoes and personal belongings
</option>

<option>
Sports equipment
</option>

<option>
Other miscellaneous items
</option>

</select>


<input
id="itemLocation"
type="text"
placeholder="Location - department / block / room"
required
>


<textarea
id="itemDescription"
placeholder="Describe where it was found or lost..."
required>
</textarea>


<input
id="itemImage"
type="file"
accept="image/*"
>


<button type="submit">
Publish Post
</button>


<p
id="postMessage"
class="message">
</p>

</form>

</div>

</div>



<!-- ======================================================
     PRIVATE REPLY MODAL
====================================================== -->

<div
id="replyModal"
class="modal hidden">

<div class="modal-box">

<button
class="close"
onclick="closeModal('replyModal')">
×
</button>


<h2>
Private Reply
</h2>


<p style="
color:#667085;
margin:10px 0;
">

Only the owner of the original post
can see the replies.

</p>


<textarea
id="replyText"
placeholder="Write your private reply...">
</textarea>


<button onclick="sendReply()">
Send Private Reply
</button>


<p
id="replyMessage"
class="message">
</p>

</div>

</div>



<!-- ======================================================
     OWNER REPLIES MODAL
====================================================== -->

<div
id="repliesModal"
class="modal hidden">

<div class="modal-box large">

<button
class="close"
onclick="closeModal('repliesModal')">
×
</button>


<h2>
Private Replies
</h2>


<div id="repliesContainer">
</div>

</div>

</div>



<script>

/*
===========================================================
SUPABASE CONFIGURATION
===========================================================

PUT YOUR SUPABASE DETAILS BELOW.

Example:

const SUPABASE_URL =
"https://abcdefgh.supabase.co";

const SUPABASE_ANON_KEY =
"eyJhbGciOiJIUzI1NiIs...";

ONLY USE THE ANON/PUBLIC KEY HERE.

NEVER PUT YOUR SERVICE_ROLE/SECRET KEY HERE.
===========================================================
*/


const SUPABASE_URL =
"PASTE_YOUR_SUPABASE_URL_HERE";


const SUPABASE_ANON_KEY =
"PASTE_YOUR_SUPABASE_ANON_KEY_HERE";


const supabaseClient =
window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_ANON_KEY
);



/* ACCESS CODE */

const ACCESS_CODE =
"Prathyusha Students";


let currentUser = null;

let selectedPostId = null;



/* ======================================================
   ACCESS
====================================================== */

function checkAccess(){

    const code =
    document
    .getElementById("accessCode")
    .value
    .trim();


    if(code === ACCESS_CODE){

        document
        .getElementById("accessPage")
        .classList.add("hidden");


        document
        .getElementById("mainPage")
        .classList.remove("hidden");


        loadPosts();

    }

    else{

        document
        .getElementById("accessError")
        .textContent =
        "Incorrect access code.";

    }

}



/* ENTER KEY */

document
.getElementById("accessCode")
.addEventListener(
"keydown",
function(e){

    if(e.key === "Enter"){

        checkAccess();

    }

});



/* ======================================================
   LOGIN
====================================================== */

function openLogin(){

    document
    .getElementById("authModal")
    .classList.remove("hidden");


    document
    .getElementById("authTitle")
    .textContent =
    "Login";


    document
    .getElementById("authButton")
    .textContent =
    "Login";


    document
    .getElementById("name")
    .classList.add("hidden");


    document
    .getElementById("forgotBtn")
    .classList.remove("hidden");


    document
    .getElementById("authMessage")
    .textContent = "";

}



/* ======================================================
   SIGN UP
====================================================== */

function openSignup(){

    document
    .getElementById("authModal")
    .classList.remove("hidden");


    document
    .getElementById("authTitle")
    .textContent =
    "Create Account";


    document
    .getElementById("authButton")
    .textContent =
    "Create Account";


    document
    .getElementById("name")
    .classList.remove("hidden");


    document
    .getElementById("forgotBtn")
    .classList.add("hidden");


    document
    .getElementById("authMessage")
    .textContent = "";

}



/* ======================================================
   AUTHENTICATION
====================================================== */

async function handleAuth(event){

    event.preventDefault();


    const email =
    document
    .getElementById("email")
    .value
    .trim();


    const password =
    document
    .getElementById("password")
    .value;


    const name =
    document
    .getElementById("name")
    .value
    .trim();


    const mode =
    document
    .getElementById("authTitle")
    .textContent;


    document
    .getElementById("authMessage")
    .textContent =
    "Please wait...";



    /* SIGN UP */

    if(mode === "Create Account"){

        const result =
        await supabaseClient
        .auth
        .signUp({

            email:email,

            password:password,

            options:{
                data:{
                    name:name
                }
            }

        });


        if(result.error){

            document
            .getElementById("authMessage")
            .textContent =
            result.error.message;

            return;

        }


        if(result.data.user){

            await supabaseClient
            .from("profiles")
            .upsert({

                id:
                result.data.user.id,

                name:name

            });

        }


        document
        .getElementById("authMessage")
        .textContent =
        "Account created successfully. You can now login.";

        return;

    }



    /* LOGIN */

    const result =
    await supabaseClient
    .auth
    .signInWithPassword({

        email:email,

        password:password

    });


    if(result.error){

        document
        .getElementById("authMessage")
        .textContent =
        result.error.message;

        return;

    }


    currentUser =
    result.data.user;


    closeModal("authModal");


    updateLoginUI();


    loadPosts();

}



/* ======================================================
   FORGOT PASSWORD
====================================================== */

async function forgotPassword(){

    const email =
    document
    .getElementById("email")
    .value
    .trim();


    if(!email){

        document
        .getElementById("authMessage")
        .textContent =
        "Enter your email first.";

        return;

    }


    const result =
    await supabaseClient
    .auth
    .resetPasswordForEmail(

        email,

        {
            redirectTo:
            window.location.origin
        }

    );


    document
    .getElementById("authMessage")
    .textContent =

    result.error
    ?
    result.error.message
    :
    "Password recovery email sent.";

}



/* ======================================================
   LOGOUT
====================================================== */

async function logout(){

    await supabaseClient
    .auth
    .signOut();


    currentUser = null;


    updateLoginUI();


    loadPosts();

}



/* ======================================================
   UPDATE LOGIN UI
====================================================== */

function updateLoginUI(){

    const login =
    document.getElementById("loginBtn");


    const signup =
    document.getElementById("signupBtn");


    const logout =
    document.getElementById("logoutBtn");


    const email =
    document.getElementById("userEmail");


    if(currentUser){

        login.classList.add("hidden");

        signup.classList.add("hidden");

        logout.classList.remove("hidden");

        email.textContent =
        currentUser.email;

    }

    else{

        login.classList.remove("hidden");

        signup.classList.remove("hidden");

        logout.classList.add("hidden");

        email.textContent = "";

    }

}



/* ======================================================
   ADD POST
====================================================== */

function openAddPost(){

    if(!currentUser){

        openLogin();

        return;

    }


    document
    .getElementById("postModal")
    .classList.remove("hidden");

}



/* ======================================================
   CREATE POST
====================================================== */

async function createPost(event){

    event.preventDefault();


    if(!currentUser){

        return;

    }


    const title =
    document
    .getElementById("itemTitle")
    .value
    .trim();


    const category =
    document
    .getElementById("itemCategory")
    .value;


    const location =
    document
    .getElementById("itemLocation")
    .value
    .trim();


    const description =
    document
    .getElementById("itemDescription")
    .value
    .trim();


    const imageFile =
    document
    .getElementById("itemImage")
    .files[0];


    let imageURL = null;


    document
    .getElementById("postMessage")
    .textContent =
    "Publishing...";



    /* UPLOAD IMAGE */

    if(imageFile){

        const extension =
        imageFile.name
        .split(".")
        .pop();


        const filePath =
        currentUser.id +
        "/" +
        crypto.randomUUID() +
        "." +
        extension;


        const upload =
        await supabaseClient
        .storage
        .from("post-images")
        .upload(
            filePath,
            imageFile
        );


        if(upload.error){

            document
            .getElementById("postMessage")
            .textContent =
            upload.error.message;

            return;

        }


        imageURL =
        supabaseClient
        .storage
        .from("post-images")
        .getPublicUrl(filePath)
        .data
        .publicUrl;

    }



    /* SAVE POST */

    const result =
    await supabaseClient
    .from("posts")
    .insert({

        user_id:
        currentUser.id,

        title:title,

        category:category,

        location:location,

        description:description,

        image_url:imageURL

    });


    if(result.error){

        document
        .getElementById("postMessage")
        .textContent =
        result.error.message;

        return;

    }


    document
    .getElementById("postMessage")
    .textContent =
    "Post published successfully!";


    event.target.reset();


    setTimeout(

        functi
create extension if not exists pgcrypto;

create table if not exists profiles (
    id uuid primary key references auth.users(id) on delete cascade,
    name text,
    created_at timestamptz default now()
);

create table if not exists posts (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    title text not null,
    category text not null,
    location text not null,
    description text not null,
    image_url text,
    created_at timestamptz default now()
);

create table if not exists replies (
    id uuid primary key default gen_random_uuid(),
    post_id uuid not null references posts(id) on delete cascade,
    user_id uuid not null references auth.users(id) on delete cascade,
    message text not null,
    created_at timestamptz default now()
);


alter table profiles enable row level security;
alter table posts enable row level security;
alter table replies enable row level security;


create policy "Anyone can view posts"
on posts
for select
using (true);


create policy "Users can create own posts"
on posts
for insert
to authenticated
with check (auth.uid() = user_id);


create policy "Users can update own posts"
on posts
for update
to authenticated
using (auth.uid() = user_id);


create policy "Users can delete own posts"
on posts
for delete
to authenticated
using (auth.uid() = user_id);


create policy "Users can create own profile"
on profiles
for insert
to authenticated
with check (auth.uid() = id);


create policy "Users can view own profile"
on profiles
for select
to authenticated
using (auth.uid() = id);


create policy "Private reply access"
on replies
for select
to authenticated
using (
    auth.uid() = user_id
    OR
    EXISTS (
        SELECT 1
        FROM posts
        WHERE posts.id = replies.post_id
        AND posts.user_id = auth.uid()
    )
);


create policy "Authenticated users can reply"
on replies
for insert
to authenticated
with check (auth.uid() = user_id);


create policy "Reply owner can delete"
on replies
for delete
to authenticated
using (auth.uid() = user_id);