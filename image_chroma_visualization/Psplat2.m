
function N = Psplat2(u, v, I, bin_step, n_bins)
ub = 1 + mod(round((u+0.4375) / bin_step), n_bins);
vb = 1 + mod(round((v+0.4375) / bin_step), n_bins);
N = reshape(accumarray(sub2ind([n_bins, n_bins], ub(:), vb(:)), I(:), ...
                               [n_bins^2, 1]), n_bins, n_bins);

%http://matlabtricks.com/post-23/tutorial-on-matrix-indexing-in-matlab
%N = zeros(n_bins,'double');
%for i = 1:n_bins
%    for j = 1:n_bins
%        
%    end
%end
