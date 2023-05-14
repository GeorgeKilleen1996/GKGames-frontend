<template>
    <div class="w-full h-screen relative">
        <div class="w-full h-screen login-right-background-red absolute top-0 right-0 bg-red-700"></div>
        <div class="w-full h-screen login-right-background-zinc absolute top-0 right-0 bg-zinc-800"></div>
        <div class="grid grid-rows-1 login-grid-cols h-screen">
            <div></div>
            <div class="w-full h-full flex justify-start items-center">
                <div class="w-5/6 bg-white shadow-md rounded-md flex flex-col gap-4 border overflow-hidden">
                    <div class="w-full h-1 bg-red-700"></div>
                    <div class="w-full text-2xl tracking-wide px-4 pt-4">Login</div>
                    <div class="w-full h-12 px-4">
                        <input type="email" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="Email Address">
                    </div>
                    <div class="w-full h-12 px-4">
                        <input type="password" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="Password">
                    </div>
                    <div class="w-full h-12 px-4">
                        <button class="w-full h-full rounded-md text-center text-red-700 border border-red-700 hover:bg-red-700 hover:text-white transition-all">Login</button>
                    </div>
                    <div class="w-full px-4 text-sm tracking-tight mb-4">
                        Are you new here? <NuxtLink to="/auth/register" class="text-red-700 hover:underline transition-all">Register an account</NuxtLink>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.login-right-background-zinc{
    clip-path: polygon(0% 0, 55% 0, 65% 100%, 0% 100%);
}
.login-right-background-red{
    clip-path: polygon(0% 0, 55.5% 0, 65.5% 100%, 0% 100%);
}
.login-grid-cols {
    grid-template-columns: 2fr 1fr;
}
</style>