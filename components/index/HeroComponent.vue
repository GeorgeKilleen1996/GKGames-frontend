<template>
    <div class="w-full max-w-[90rem] relative">
        <div class="w-full h-full bg-red-700 absolute top-0 right-0 hero-right-background-red"></div>
        <div class="w-full h-full bg-zinc-800 absolute top-0 right-0 hero-right-background-slate"></div>
        <div class="w-full h-[50rem] mx-auto grid grid-cols-2 grid-rows-1">
            <div class="relative">
                <div class="w-full h-full md:pl-10 pl-2"></div>
            </div>
            <div class="relative">
                <div class="w-full h-full md:pr-10 pr-2"></div>
            </div>
        </div>
    </div>
</template>

<style>
.hero-right-background-slate{
    clip-path: polygon(64.5% 0, 100% 0, 100% 100%, 44.5% 100%);
}

.hero-right-background-red{
    clip-path: polygon(64% 0, 100% 0, 100% 100%, 44% 100%);
}
</style>