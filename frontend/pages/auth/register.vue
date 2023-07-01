<script setup>
const config = useRuntimeConfig();

const first_name = ref('');
const last_name = ref('');
const email = ref('');
const password = ref('');
const confirm_password = ref('');

const registerUser = () => {
    if(first_name.value == '' || last_name.value == '' || email.value == '' || password.value == '' || confirm_password.value == ''){
        alert('Please fill all the fields'); // changed from an alert to a toast
    } else {
        if(password.value != confirm_password.value){
            alert('Password and Confirm Password do not match'); // changed from an alert to a toast
        } else {
            fetch(config.public.api.baseUrl + `auth/register/`, {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: email.value,
                    password: password.value,
                    first_name: first_name.value,
                    last_name: last_name.value,
                }),
            }).then(response => {
                console.log(response);
            });
        }
    }
}
</script>
<template>
    <div class="w-full h-screen relative">
        <div class="flex flex-row w-full h-full">
            <div class="w-1/3 h-full bg-neutral-100 drop-shadow-sm flex justify-center items-center">
                <div class="w-4/5 flex flex-col justify-center items-center gap-8">
                    <div class="text-xl tracking-wider uppercase text-neutral-500">Create an account</div>
                    <div class="w-full flex gap-6">
                        <div class="w-1/2 h-12">
                            <input type="text" placeholder="First Name" class="w-full h-full rounded-md px-4">
                        </div>
                        <div class="w-1/2 h-12">
                            <input type="text" placeholder="Last Name" class="w-full h-full rounded-md px-4">
                        </div>
                    </div>
                    <div class="w-full h-12">
                        <input type="text" placeholder="Email Address" class="w-full h-full rounded-md px-4">
                    </div>
                    <div class="w-full h-12">
                        <input type="text" placeholder="Password" class="w-full h-full rounded-md px-4">
                    </div>
                    <div class="w-full h-12">
                        <input type="text" placeholder="Confirm Password" class="w-full h-full rounded-md px-4">
                    </div>
                    <button class="w-full h-12 rounded-md bg-gradient-to-br from-teal-400 to-teal-500 text-white uppercase">Sign Up</button>
                </div>
            </div>
            <div class="w-2/3 h-full"></div>
        </div>
    </div>
</template>

<style>
.register-right-background-zinc{
    clip-path: polygon(45% 0, 100% 0, 100% 100%, 35% 100%);
}
.register-right-background-red{
    clip-path: polygon(44.5% 0, 100% 0, 100% 100%, 34.5% 100%);
}
.register-grid-cols {
    grid-template-columns: 1fr 2fr;
}
</style>