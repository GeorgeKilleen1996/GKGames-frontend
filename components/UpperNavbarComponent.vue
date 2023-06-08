<template>
    <div>
        <div class="w-full max-w-[90rem] md:px-10 px-2 mx-auto bg-white pt-[1.5rem] pb-[1rem]">
            <div class="w-full h-full flex items-center h-16">
                <div class="flex flex-row items-center justify-center lg:w-1/6">
                    <h1 class="font-semibold tracking-tighter text-3xl pl-2 uppercase font-semibold">GK Games</h1>
                </div>
                <div class="h-full lg:w-4/6 relative px-4">
                    <input type="text" class="w-full h-full rounded-full bg-neutral-50 p-4 pl-10 placeholder-neutral-500" placeholder="SEARCH">
                    <i class="fas fa-magnifying-glass text-neutral-500 absolute left-8 top-4 text-sm"></i>
                </div>
                <div class="flex flex-row items-center text-neutral-500 lg:w-1/6">
                    <div class="grid grid-cols-2 grid-rows-1">
                        <div class="flex justify-end items-center">
                            <i class="fas fa-user text-xl pr-1"></i>
                        </div>
                        <div class="tracking-wide text-xs font-light flex flex-col items-start justify-center pl-1 leading-tight">
                            <NuxtLink to="/auth/login" class="hover:text-black cursor-pointer transition-all">Sign In</NuxtLink>
                            <span class="font-medium hover:text-black cursor-pointer transition-all">Account</span>
                        </div>
                    </div>
                    <div class="grid grid-cols-2 grid-rows-1 hover:text-black cursor-pointer transition-all">
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
    </div>
</template>