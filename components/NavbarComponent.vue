<script setup>
</script>
<template>
    <div class="w-full h-16 max-w-[90rem] md:px-10 px-2 mx-auto fixed top-0 z-50">
        <div class="w-full h-full flex justify-between items-center">
            <div class="flex flex-row items-center">
                <div class="w-12 h-12 rounded-full flex justify-center items-center bg-red-700 text-white font-semibold text-xl">
                    GK
                </div>
                <h1 class="font-semibold tracking-tight text-3xl pl-2">Games</h1>
            </div>
            <div class="flex flex-row items-center text-neutral-300">
                <div class="cursor-pointer hover:text-white transition-all">
                    <i class="fas fa-magnifying-glass text-xl"></i>
                </div>
                <div class="grid grid-cols-2 grid-rows-1">
                    <div class="flex justify-end items-center">
                        <i class="fas fa-user text-xl pr-1"></i>
                    </div>
                    <div class="tracking-wide text-xs font-light flex flex-col items-start justify-center pl-1 leading-tight">
                        <NuxtLink to="/auth/login" class="hover:text-white cursor-pointer transition-all">Sign In</NuxtLink>
                        <span class="font-medium hover:text-white cursor-pointer transition-all">Account</span>
                    </div>
                </div>
                <div class="grid grid-cols-2 grid-rows-1 hover:text-white cursor-pointer transition-all">
                    <div class="flex justify-end items-center">
                        <i class="fas fa-cart-shopping text-xl pr-1"></i>
                    </div>
                    <div class="tracking-wide text-sm font-light flex items-center justify-start pl-1">
                        £0.00
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>