<template>
    <div class="w-full h-screen relative">
        <div class="w-full h-screen register-right-background-red absolute top-0 right-0 bg-red-700"></div>
        <div class="w-full h-screen register-right-background-zinc absolute top-0 right-0 bg-zinc-800"></div>
        <div class="grid grid-rows-1 register-grid-cols h-screen">
            <div class="w-full h-full flex justify-end items-center">
                <div class="w-5/6 bg-white shadow-md rounded-md flex flex-col gap-4 border overflow-hidden">
                    <div class="w-full h-1 bg-red-700"></div>
                    <div class="w-full text-2xl tracking-wide px-4 pt-4">Register</div>
                    <div class="w-full flex flex-row gap-4 px-4">
                        <div class="w-1/2 h-12">
                            <input type="text" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="First Name">
                        </div>
                        <div class="w-1/2 h-12">
                            <input type="text" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="Last Name">
                        </div>
                    </div>
                    <div class="w-full h-12 px-4">
                        <input type="email" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="Email Address">
                    </div>
                    <div class="w-full h-12 px-4">
                        <input type="password" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="Password">
                    </div>
                    <div class="w-full h-12 px-4">
                        <input type="password" class="w-full h-full rounded-md border px-2 focus:outline-none focus:ring-2 focus:ring-red-700" placeholder="Confirm Password">
                    </div>
                    <div class="w-full h-12 px-4 mb-4">
                        <button class="w-full h-full rounded-md text-center text-red-700 border border-red-700 hover:bg-red-700 hover:text-white transition-all">Register</button>
                    </div>
                </div>
            </div>
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