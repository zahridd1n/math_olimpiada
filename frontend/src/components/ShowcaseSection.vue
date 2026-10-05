<template>
  <section id="natijalar" class="editorial-section certificate-gallery-section">
    <div class="container">
      <!-- Section Header -->
      <div class="gallery-header">
        <div class="header-kicker">
          <span class="editorial-label">Yutuqlar & Natijalar</span>
          <span class="editorial-tag">[ Galereya ]</span>
        </div>
        <h2 class="gallery-title">
          O'quvchilarimiz <span class="serif-italic-gold">yutuqlari</span> va <span class="serif-italic">sertifikatlari</span>
        </h2>
        <p class="gallery-sub">
          O'quvchilarimiz erishgan muvaffaqiyatlar, sertifikatlar va diplomlar galereyasi.
        </p>
      </div>

      <!-- Certificate Carousel Container -->
      <div class="carousel-wrapper" v-if="items.length > 0">
        <div class="carousel-viewport">
          <div 
            class="carousel-track" 
            :style="{ transform: `translateX(-${currentIndex * (cardWidthPercent)}%)` }"
          >
            <div 
              v-for="(item, idx) in items" 
              :key="item.id || idx" 
              class="carousel-slide"
              @click="openLightbox(item.image_url || item.image)"
            >
              <div class="certificate-card">
                <img 
                  :src="item.image_url || item.image" 
                  :alt="item.title || 'Olimpiada sertifikati'" 
                  class="cert-image" 
                  loading="lazy"
                />
                <div class="cert-overlay">
                  <span class="zoom-hint">Kattalashtirib ko'rish 🔍</span>
                </div>
                <div v-if="item.title" class="cert-caption">
                  <span class="cert-title">{{ item.title }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Carousel Navigation Controls -->
        <div class="carousel-controls">
          <button 
            @click="prevSlide" 
            class="carousel-btn" 
            :disabled="currentIndex === 0"
            aria-label="Oldingi"
          >
            <span>←</span>
          </button>
          
          <div class="carousel-indicators">
            <span 
              v-for="(_, i) in maxIndex + 1" 
              :key="i" 
              class="indicator-dot" 
              :class="{ active: currentIndex === i }"
              @click="currentIndex = i"
            ></span>
          </div>

          <button 
            @click="nextSlide" 
            class="carousel-btn" 
            :disabled="currentIndex >= maxIndex"
            aria-label="Keyingi"
          >
            <span>→</span>
          </button>
        </div>
      </div>

      <!-- Empty State (When no images uploaded from Django admin yet) -->
      <div v-else class="empty-gallery-box">
        <div class="empty-inner">
          <span class="empty-icon">📜</span>
          <h3 class="empty-title">Sertifikatlar tez orada joylanadi</h3>
          <p class="empty-desc">
            Rasmiy sertifikat va diplom namunalari Django Admin paneli orqali yuklanadi.
          </p>
        </div>
      </div>
    </div>

    <!-- Lightbox Modal for Full View -->
    <transition name="fade">
      <div v-if="lightboxImg" class="lightbox-modal" @click.self="lightboxImg = null">
        <button class="lightbox-close" @click="lightboxImg = null" aria-label="Yopish">✕</button>
        <img :src="lightboxImg" alt="Sertifikat to'liq ko'rinishi" class="lightbox-full-img" />
      </div>
    </transition>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { getCertificates } from '../services/api.js'

const items = ref([])
const currentIndex = ref(0)
const lightboxImg = ref(null)
const visibleCount = ref(3)

function updateVisibleCount() {
  if (window.innerWidth < 640) {
    visibleCount.value = 1
  } else if (window.innerWidth < 1024) {
    visibleCount.value = 2
  } else {
    visibleCount.value = 3
  }
}

const cardWidthPercent = computed(() => {
  return 100 / visibleCount.value
})

const maxIndex = computed(() => {
  return Math.max(0, items.value.length - visibleCount.value)
})

function prevSlide() {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}

function nextSlide() {
  if (currentIndex.value < maxIndex.value) {
    currentIndex.value++
  }
}

function openLightbox(url) {
  if (url) {
    lightboxImg.value = url
  }
}

onMounted(async () => {
  updateVisibleCount()
  window.addEventListener('resize', updateVisibleCount)

  const certs = await getCertificates()
  if (certs && certs.length > 0) {
    items.value = certs
  }
})
</script>

<style scoped>
.certificate-gallery-section {
  background-color: var(--bg-section-2);
  position: relative;
  overflow: hidden;
}

.gallery-header {
  max-width: 760px;
  margin-bottom: 56px;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.gallery-title {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 700;
  line-height: 1.16;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 18px;
}

.gallery-sub {
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--text-secondary);
}

/* Carousel */
.carousel-wrapper {
  position: relative;
  width: 100%;
}

.carousel-viewport {
  overflow: hidden;
  width: 100%;
  border-radius: 16px;
  padding: 10px 0;
}

.carousel-track {
  display: flex;
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  gap: 0px;
}

.carousel-slide {
  flex: 0 0 calc(100% / 3);
  padding: 0 14px;
  box-sizing: border-box;
}

@media (max-width: 1024px) {
  .carousel-slide {
    flex: 0 0 50%;
  }
}

@media (max-width: 640px) {
  .carousel-slide {
    flex: 0 0 100%;
  }
}

.certificate-card {
  position: relative;
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  aspect-ratio: 1.4 / 1;
  display: flex;
  flex-direction: column;
}

.certificate-card:hover {
  transform: translateY(-4px);
  border-color: var(--gold);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
}

.cert-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.certificate-card:hover .cert-image {
  transform: scale(1.03);
}

.cert-overlay {
  position: absolute;
  inset: 0;
  background: rgba(6, 8, 20, 0.6);
  backdrop-filter: blur(4px);
  opacity: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.3s ease;
}

.certificate-card:hover .cert-overlay {
  opacity: 1;
}

.zoom-hint {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  letter-spacing: 0.08em;
  color: var(--gold);
  padding: 6px 14px;
  background: rgba(6, 8, 20, 0.85);
  border: 1px solid var(--border-subtle);
  border-radius: 999px;
}

.cert-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px 14px;
  background: linear-gradient(180deg, transparent 0%, rgba(6, 8, 20, 0.95) 100%);
}

.cert-title {
  font-size: 0.85rem;
  color: #ffffff;
  font-weight: 600;
}

/* Controls */
.carousel-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 36px;
}

.carousel-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-medium);
  color: #ffffff;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.carousel-btn:hover:not(:disabled) {
  background: var(--gold);
  color: #060814;
  border-color: var(--gold);
}

.carousel-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.carousel-indicators {
  display: flex;
  gap: 8px;
}

.indicator-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  cursor: pointer;
  transition: all 0.2s ease;
}

.indicator-dot.active {
  background: var(--gold);
  width: 24px;
  border-radius: 4px;
}

/* Empty State */
.empty-gallery-box {
  border: 1px dashed var(--border-medium);
  border-radius: 16px;
  padding: 60px 24px;
  text-align: center;
  background: rgba(255, 255, 255, 0.015);
}

.empty-icon {
  font-size: 2.5rem;
  display: block;
  margin-bottom: 12px;
}

.empty-title {
  font-size: 1.25rem;
  color: #ffffff;
  margin-bottom: 8px;
}

.empty-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  max-width: 440px;
  margin: 0 auto;
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.9);
  backdrop-filter: blur(10px);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.lightbox-full-img {
  max-width: 90vw;
  max-height: 85vh;
  object-fit: contain;
  border-radius: 10px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
  border: 1px solid var(--border-medium);
}

.lightbox-close {
  position: absolute;
  top: 24px;
  right: 24px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid var(--border-medium);
  color: #ffffff;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.lightbox-close:hover {
  background: var(--gold);
  color: #060814;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
