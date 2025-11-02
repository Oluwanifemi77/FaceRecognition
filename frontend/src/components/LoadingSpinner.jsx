import React from 'react';
import { motion } from 'framer-motion';

const LoadingSpinner = ({ message = 'Processing...' }) => {
  return (
    <div className="flex flex-col items-center justify-center p-12">
      {/* Outer Rotating Ring */}
      <div className="relative">
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1.5, repeat: Infinity, ease: 'linear' }}
          className="w-20 h-20 border-4 border-cyan-500/30 border-t-cyan-500 rounded-full"
          style={{ filter: 'drop-shadow(0 0 10px rgba(34, 211, 238, 0.5))' }}
        />

        {/* Inner Counter-Rotating Ring */}
        <motion.div
          animate={{ rotate: -360 }}
          transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
          className="absolute inset-2 border-4 border-purple-500/30 border-b-purple-500 rounded-full"
          style={{ filter: 'drop-shadow(0 0 10px rgba(167, 139, 250, 0.5))' }}
        />

        {/* Center Pulse */}
        <motion.div
          animate={{
            scale: [1, 1.2, 1],
            opacity: [0.5, 1, 0.5],
          }}
          transition={{ duration: 1.5, repeat: Infinity }}
          className="absolute inset-6 bg-gradient-to-r from-cyan-500 to-purple-500 rounded-full blur-sm"
        />
      </div>

      {/* Animated Message */}
      <motion.p
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="mt-6 text-gray-300 font-semibold text-lg"
      >
        {message}
      </motion.p>

      {/* Animated Dots */}
      <div className="flex gap-2 mt-4">
        {[0, 1, 2].map((index) => (
          <motion.div
            key={index}
            className="w-2 h-2 bg-gradient-to-r from-cyan-400 to-purple-400 rounded-full"
            animate={{
              scale: [1, 1.5, 1],
              opacity: [0.5, 1, 0.5],
            }}
            transition={{
              duration: 1,
              repeat: Infinity,
              delay: index * 0.2,
            }}
          />
        ))}
      </div>
    </div>
  );
};

export default LoadingSpinner;
