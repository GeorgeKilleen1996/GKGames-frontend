<template>
    <div class="w-full max-w-[90rem] mx-auto py-[2.5rem] lg:px-10">
        <div class="flex flex-col gap-8">
            <!-- Section title -->
            <div class="uppercase text-lg tracking-wider leading-relaxed font-semibold">Popular Items</div>
            <div class="w-full h-0.5 bg-neutral-100"></div>
            <!-- Popular items -->
            <div class="w-full grid grid-cols-5 gap-4">
                <div class="w-full h-[20rem] flex flex-col overflow-hidden" v-for="i in 5">
                    <div class="w-full h-2/3 bg-neutral-100 flex justify-center items-center p-4 rounded-2xl">
                        product image
                    </div>
                    <div class="w-full h-1/3 flex justify-center items-center p-4">
                        product info
                    </div>
                </div>
            </div>
            <div class="w-full h-9 flex justify-end items-center">
                <div class="h-full rounded-full bg-neutral-100 px-2 flex flex-row items-center gap-2 cursor-pointer hover:scale-[1.05] hover:bg-neutral-200 transition-all">
                    <div class="text-sm">View All</div>
                    <div><i class="fas fa-arrow-right text-xs mb-1"></i></div>
                </div>
            </div>
        </div>
    </div>
</template>