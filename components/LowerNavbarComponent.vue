<script setup>
const navButtonHovered = ref('');
</script>
<template>
    <div class="w-full h-12 max-w-[90rem] mx-auto flex justify-center items-center">
        <div class="flex flex-row gap-6">
            <!-- Pokemon Nav Item -->
            <div @mouseover="navButtonHovered = 'Pokemon'" @mouseleave="navButtonHovered = ''">
                <NuxtLink class="text-black text-sm flex flex-row gap-2 font-semibold items-center cursor-pointer">
                    <div>Pokemon</div>
                    <div><i class="fas fa-caret-down text-[10px] transition-all" :class="{'rotate-180 text-black' : navButtonHovered == 'Pokemon', 'text-neutral-400' : navButtonHovered != 'Pokemon'}"></i></div>
                </NuxtLink>
            </div>
            <!-- Clothing & Accessories Nav Item -->
            <div @mouseover="navButtonHovered = 'Accessories'" @mouseleave="navButtonHovered = ''">
                <NuxtLink class="text-black text-sm flex flex-row gap-2 font-semibold items-center cursor-pointer">
                    <div>Clothing & Accessories</div>
                    <div><i class="fas fa-caret-down text-[10px] transition-all" :class="{'rotate-180 text-black' : navButtonHovered == 'Accessories', 'text-neutral-400' : navButtonHovered != 'Accessories'}"></i></div>
                </NuxtLink>
            </div>
            <!-- Sale Nav Item -->
            <div @mouseover="navButtonHovered = 'Sale'" @mouseleave="navButtonHovered = ''">
                <NuxtLink class="text-red-700 text-sm flex flex-row gap-2 font-semibold items-center cursor-pointer">
                    <div>Sale</div>
                    <div><i class="fas fa-caret-down text-[10px] transition-all text-red-700" :class="{'rotate-180' : navButtonHovered == 'Sale'}"></i></div>
                </NuxtLink>
            </div>
            <!-- Sell to us Nav Item -->
            <div>
                <NuxtLink class="text-black text-sm flex flex-row gap-2 font-semibold items-center cursor-pointer">
                    <div>Sell to us</div>
                </NuxtLink>
            </div>
            <!-- Blog Nav Item -->
            <div>
                <NuxtLink class="text-black text-sm flex flex-row gap-2 font-semibold items-center cursor-pointer">
                    <div>Blog</div>
                </NuxtLink>
            </div>
        </div>
    </div>
</template>